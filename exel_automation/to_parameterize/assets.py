import json


"""枚举"""
from exel_automation.to_parameterize.GloaEnum import GloablEnum
"""日志"""
from exel_automation.getfile.assets import FileInformation
from log.assets import Logger

log_path, config_path = FileInformation.get_data()
logger = Logger(log_dir=log_path)
adminUrl, clientUrl, excelPath = FileInformation.configpath_json()


class ParameterReplacer:

    @staticmethod
    def replace_parameters(body, params, data):
        body_str = json.dumps(body)  # Convert body dictionary to a string
        for param in params:
            logger.debug(f'查询params参数内容：{params}')
            logger.debug(f'查询params参数的类型：{type(params)}')
            param_name = param["paramName"]
            param_value = ParameterReplacer.get_param_value(param["paramsEq"], data)
            if param_value is not None:
                body_str = body_str.replace("${" + param_name + "}", str(param_value))
        body = json.loads(body_str)  # Convert the updated string back to a dictionary
        return body

    @staticmethod
    def get_param_value(expression, data):
        try:
            parts = expression.split('.')
            value = data
            for part in parts:
                if '[' in part:
                    key, index = part.split('[')
                    index = int(index.strip(']'))
                    value = value[key][index]
                else:
                    value = value[part]
            return value
        except (KeyError, IndexError, TypeError):
            return None
