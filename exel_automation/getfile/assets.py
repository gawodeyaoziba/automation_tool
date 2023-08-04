
"""接口url"""
from Config.config import swagger_assets_url

"""模块"""
from utils.my_third_party_modules import requests, json

class FileInformation:
    @staticmethod
    def get_data():
        """
        获取服务器响应地址
        :return:
        """
        try:
            response = requests.get(url=swagger_assets_url)
            configuration_data = json.loads(response.text)
            return configuration_data
        except:
            print('检查服务器/路由')

    """遍历响应文件"""
    def other_function(self, field_name):
        """
        获取配置表子内容信息
        :param field_name: 读取config配置文件表格主内容
        :return: 配置表对应子内容
        """
        configurationdata = self.get_data()
        if isinstance(configurationdata, dict):
            for key, value in configurationdata.items():
                if isinstance(value, dict):
                    for inner_key, inner_value in value.items():
                        if inner_key == field_name:
                            return inner_value

















