import json
import re
from copy import deepcopy

from log.assets import Logger

logger = Logger()


class ToParameterize:

    def replace_parameters(self, data, parameters, response_body):
        """
        替换数据中的参数
        Args:
            data (dict): 待处理的数据
            parameters (list): 参数列表
            response_body (dict): 响应体
        Returns:
            dict: 替换后的数据
        """
        updated_data = deepcopy(data)
        replacements = []  # 存储匹配到的参数及其替换值

        for key, value in updated_data.items():
            if isinstance(value, str):
                for param in parameters:
                    parameter_name = param['paramName']
                    parameter_from = param['paramFrom']
                    parameter_eq = param['paramsEq']
                    if f"${{{parameter_name}}}" in value:
                        if parameter_from in ('responseBody', 'requestBody'):
                            patterns = [
                                re.compile(rf'"{re.escape(parameter_eq)}"\s*:\s*"(.*?)"'),  # 匹配{}
                                re.compile(rf'"{re.escape(parameter_eq)}"\s*:\s*([\d.]+)')  # 匹配}}}
                            ]

                            if parameter_from == 'responseBody':
                                matches = self.find_matches(patterns, json.dumps(response_body))
                            else:
                                matches = self.find_matches(patterns, json.dumps(updated_data))

                            replacements.extend([(f"${{{parameter_name}}}", match) for match in matches])

        # 替换所有匹配到的参数
        for placeholder, replacement in replacements:
            updated_data = self.replace_all(updated_data, placeholder, replacement)

        updated_data = self.execute_functions(updated_data)

        return updated_data

    def find_matches(self, patterns, text):
        """
        查找正则表达式的匹配项
        Args:
            patterns (list): 正则表达式模式列表
            text (str): 待匹配的文本
        Returns:
            list: 匹配到的结果列表
        """
        matches = []
        for pattern in patterns:
            matches.extend(pattern.findall(text))
        return matches

    def replace_all(self, data, placeholder, replacement):
        """
        迭代替换数据中的占位符
        Args:
            data (dict or list): 待处理的数据
            placeholder (str): 占位符
            replacement (str): 替换值
        Returns:
            dict or list: 替换后的数据
        """
        stack = [(data, None)]
        while stack:
            current, parent_key = stack.pop()
            if isinstance(current, dict):
                for key, value in current.items():
                    if isinstance(value, str):
                        current[key] = value.replace(placeholder, replacement)
                    elif isinstance(value, (dict, list)):
                        stack.append((value, key))
            elif isinstance(current, list):
                for i, item in enumerate(current):
                    stack.append((item, i))
                if parent_key is not None:
                    current[parent_key] = [item for item in current if not isinstance(item, str)]
        return data

    def execute_functions(self, data):
        """
        执行#{dama_}函数内容
        Args:
            data (dict): 待处理的数据
        Returns:
            int or None: 执行函数后的数值，如果没有匹配结果则返回 None
        """
        updated_value = None  # 初始化 updated_value
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str) and "#{" in value:
                    function_names = re.findall(r'\#\{(.+?)\}', value)  # 非贪婪匹配获取所有满足条件的函数名
                    for function_name in function_names:
                        if function_name.startswith("dama_"):
                            try:
                                matches = re.findall(r'([\d.]+)\#\{dama_(\d+)\}', value)  # 提取数值和替换值
                                for match in matches:
                                    number_before_hash = float(match[0])  # 获取#前面的数值
                                    replacement = int(match[1])  # 获取替换值
                                    updated_value = number_before_hash + replacement  # 将数值和替换值相加
                            except ValueError:
                                # 如果无法将数值或替换值转换为浮点数或整数，则保持原样
                                print('请输入数字')

        if updated_value is not None:
            # 替换所有匹配到的占位符
            for key, value in data.items():
                if isinstance(value, str):
                    data[key] = re.sub(r'([\d.]+)\#\{dama_(\d+)\}', str(updated_value), value)

        return data


