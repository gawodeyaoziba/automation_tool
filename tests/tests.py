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

        # 执行#{dama_}函数内容
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
        递归替换数据中的占位符
        Args:
            data (dict or list): 待处理的数据
            placeholder (str): 占位符
            replacement (str): 替换值
        Returns:
            dict or list: 替换后的数据
        """
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str):
                    data[key] = value.replace(placeholder, replacement)
                elif isinstance(value, (dict, list)):
                    data[key] = self.replace_all(value, placeholder, replacement)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                data[i] = self.replace_all(item, placeholder, replacement)
        return data

    def execute_functions(self, data):
        """
        执行#{dama_}函数内容
        Args:
            data (dict): 待处理的数据
        Returns:
            dict: 执行函数后的数据
        """
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str) and "#{" in value:
                    function_name = re.search(r'\#\{(.+?)\}', value).group(1)
                    # 执行相应的函数内容
                    if function_name.startswith("dama_"):
                        replacement = function_name  # 使用提取到的值作为替换值
                        data[key] = value.replace("#{" + function_name + "}", str(replacement))
                elif isinstance(value, (dict, list)):
                    data[key] = self.execute_functions(value)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                data[i] = self.execute_functions(item)
        return data
