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
                            pattern = rf"\"{re.escape(param_eq)}\"\s*:\s*\"([^\"]+)\""
                            match = re.search(pattern, json.dumps(response_body))
                            if match:
                                replacements.append((f"${{{param_name}}}", match.group(1)))
                        elif param_from == 'requestBody':
                            match = re.search(rf"\"{re.escape(param_eq)}\"\s*:\s*\"([^\"]+)\"",
                                              json.dumps(updated_data))
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
