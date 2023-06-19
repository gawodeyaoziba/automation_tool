
"""接口url"""
from exel_automation.getfile.config import swagger_assets_url


"""模块"""
import requests
import json

class FileInformation:

    """获取服务器响应地址"""
    def get_data(self):
        try:
            response = requests.get(url=swagger_assets_url)
            configuration_data = json.loads(response.text)
            return configuration_data
        except:
            print('检查服务器/路由')

    """遍历响应文件"""
    def other_function(self, field_name):
        configurationdata = self.get_data()
        if isinstance(configurationdata, dict):
            for key, value in configurationdata.items():
                if isinstance(value, dict):
                    for inner_key, inner_value in value.items():
                        if inner_key == field_name:
                            return inner_value

















