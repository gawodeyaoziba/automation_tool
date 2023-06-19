"""枚举"""
from GloaEnum.GloaEnum import FILEINFORMATION
"""配置文件"""
from exel_automation.getfile.assets import FileInformation
FileInformation = FileInformation()
"""日志"""
from log.assets import Logger
logger = Logger()
"""模块"""
import json

"""遍历config.json文件"""
class ConfigurationFile:
    def __init__(self):
        self.configPath = FileInformation.other_function(FILEINFORMATION.CONFIGPATH.value)

    def configuration_file(self, field_name):
        with open(self.configPath, "r") as configPath_json:
            configPath_data = json.load(configPath_json)
            if isinstance(configPath_data, dict):
                for key, value in configPath_data.items():
                    if key == field_name:
                        return value

