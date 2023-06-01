import requests
import json

"""接口url"""
from exel_automation.getfile.config import swagger_assets_url
"""枚举"""
from exel_automation.getfile.GloaEnum import GloablEnum
"""日志"""
from log.assets import Logger

class FileInformation:
    log_path = None
    config_path = None

    @staticmethod
    def get_data():
        response = requests.get(url=swagger_assets_url)
        data = json.loads(response.text)
        log_path = data.get(GloablEnum.DATA.value, {}).get(GloablEnum.LOGPATH.value)
        config_path = data.get(GloablEnum.DATA.value, {}).get(GloablEnum.CONFIGPATH.value)
        if not log_path or not config_path:
            error_msg = GloablEnum.GET_DATA_ERROR_MSG.value
            raise Exception(error_msg)
        FileInformation.log_path = log_path
        FileInformation.config_path = config_path
        return log_path, config_path

    @staticmethod
    def configpath_json():
        if not FileInformation.config_path:
            print(GloablEnum.CONFIGPATH_JSON_PRINT.value)
            return

        logger = Logger(log_dir=FileInformation.log_path)
        if not FileInformation.log_path:
            FileInformation.log_path = GloablEnum.DEFAULT_LOG_PATH.value  # Set a default value

        with open(FileInformation.config_path, GloablEnum.R.value) as configpath_json:
            configpath_jsona = json.load(configpath_json)
            logger.debug(f'{GloablEnum.CONFIGPATH_JSON_LOGGER.value}{configpath_jsona}')
            adminUrl = configpath_jsona.get(GloablEnum.ADMINURL.value)
            clientUrl = configpath_jsona.get(GloablEnum.CLIENTURL.value)
            excelPath = configpath_jsona.get(GloablEnum.EXECELPATH.value)
            if not adminUrl or not clientUrl or not excelPath:
                error_msg = GloablEnum.CONFIGPATH_JSON_ERROR_MSG.value
                raise Exception(error_msg)
            return adminUrl, clientUrl, excelPath


















