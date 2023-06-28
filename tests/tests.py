
"""
1. 兼容${}函数
2. 增加#{}函数
4. 可能出现的情况：
	情况一：${}#{dama_}
	情况二：${}#{dama_${}}
需求解析：
	1. ${}进行替换后再执行#{dama_}函数内容
	2. #{dama_}在${}占位成数字后，进行增加#{dama_}内容
		情况一原理解析：
			${aaa}#{dama_33}
			解析：${aaa}替换成：100
			100#{dama_33}解析#{dama_33} = 33
			100+33 = 133
			再次进行占位符替换
		情况二原理解析：
			${aaa}#{dama_${bbb}}
			解析：
				${aaa}替换成：100
				${bbb}替换成：1
			100#{dama_1}解析#{dama_1} = 1
			100+1 = 101
			再次进行占位符替换
operations = re.findall(r'\#\{(.+?)\}', value)
"""



import json
import re

"""日志"""
from log.assets import Logger

logger = Logger()


class ToParameterize:
    def replace_parameters(self, data, parameters, response_body):
        updated_data = json.loads(json.dumps(data))
        replacements = []  # 存储匹配到的参数及其替换值

        for key, value in updated_data.items():
            if isinstance(value, str):
                for param in parameters:
                    param_name = param['paramName']
                    param_from = param['paramFrom']
                    param_eq = param['paramsEq']
                    if f"${{{param_name}}}" in value:
                        if param_from == 'responseBody':
                            patterns = [
                                rf'"{re.escape(param_eq)}"\s*:\s*"(.*?)"',  # 匹配{}
                                rf'"{re.escape(param_eq)}"\s*:\s*([\d.]+)'  # 匹配{{{{{}}}}}

                            ]

                            for pattern in patterns:
                                matches = re.findall(pattern, json.dumps(response_body))
                                if matches:
                                    replacements.extend([(f"${{{param_name}}}", match) for match in matches])

                        elif param_from == 'requestBody':
                            patterns = [
                                rf'"{re.escape(param_eq)}"\s*:\s*"(.*?)"',  # 匹配{}
                                rf'"{re.escape(param_eq)}"\s*:\s*([\d.]+)'  # 匹配{{{{{}}}}}

                            ]

                            for pattern in patterns:
                                match = re.search(pattern, json.dumps(updated_data))
                                if match:
                                    replacements.append((f"${{{param_name}}}", match.group(1)))

        # 替换所有匹配到的参数
        for placeholder, replacement in replacements:
            updated_data = self.replace_all(updated_data, placeholder, replacement)

        return updated_data

    def replace_all(self, data, placeholder, replacement):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str):
                    data[key] = value.replace(placeholder, replacement)
                elif isinstance(value, (dict, list)):
                    data[key] = self.replace_all(value, placeholder, replacement)
        elif isinstance(data, list):
            for i in range(len(data)):
                data[i] = self.replace_all(data[i], placeholder, replacement)
        return data
