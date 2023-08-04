"""枚举"""
from GloaEnum.GloaEnum import FILEINFORMATION
"""配置文件"""
from exel_automation.getfile.assets import FileInformation
FileInformation = FileInformation()
"""日志"""
from log.assets import Logger
logger = Logger()
"""模块"""
from utils.my_third_party_modules import json

"""遍历config.json文件"""
class ConfigurationFile:

    def __init__(self):
        """
        :param CONFIGPATH : 枚举【获取配置文件路径信息】
        """
        self.configPath = FileInformation.other_function(FILEINFORMATION.CONFIGPATH.value)

    def configuration_file(self, field_name):
        """
        遍历配置文件信息
        :param field_name: 获取配置文件路径信息
        :return:
        """
        with open(self.configPath, "r") as configPath_json:
            configPath_data = json.load(configPath_json)
            if isinstance(configPath_data, dict):
                for key, value in configPath_data.items():
                    if key == field_name:
                        print(value)
                        return value

