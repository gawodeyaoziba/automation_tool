import json
import re
class ToParameterize:
    def replace_parameters(self, data, parameters, response_body):
        updated_data = json.loads(json.dumps(data))

        for key, value in updated_data.items():
            # print(value)
            if isinstance(value, str):
                for param in parameters:
                    param_name = param['paramName']
                    param_from = param['paramFrom']
                    param_eq = param['paramsEq']
                    if f"${{{param_name}}}" in value:
                        if param_from == 'responseBody':
                            matched_values = []
                            pattern = rf"\"{re.escape(param_eq)}\"\s*:\s*\"([^\"]+)\""
                            match = re.search(pattern, json.dumps(response_body))
                            if match:
                                updated_data[key] = value.replace(f"${{{param_name}}}", match.group(1))
                        elif param_from == 'requestBody':
                            match = re.search(rf"\"{re.escape(param_eq)}\"\s*:\s*\"([^\"]+)\"",
                                              json.dumps(updated_data))
                            if match:
                                updated_data[key] = value.replace(f"${{{param_name}}}", match.group(1))
        return updated_data