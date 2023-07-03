import yaml
"""枚举"""
from GloaEnum.GloaEnum import FILEINFORMATION
"""日志路径"""
from exel_automation.getfile.assets import FileInformation
FileInformation = FileInformation()

class ClashProxyHandler:
    config_file_path = FileInformation.other_function(FILEINFORMATION.PROXYCONFIGPATH.value)
    def __init__(self):
        self.proxies = self._load_proxies()

    def _load_proxies(self):
        with open(self.config_file_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config.get('proxies', {})

    def get_proxies(self):
        return self.proxies[0] if self.proxies else {}

