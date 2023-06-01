from exel_automation.getfile.assets import FileInformation
from log.assets import Logger

log_path, config_path = FileInformation.get_data()
logger = Logger(log_dir=log_path)
adminUrl, clientUrl, excelPath = FileInformation.configpath_json()


if __name__ == '__main__':
    try:
        log_path, config_path = FileInformation.get_data()
        logger.info(f"log_path: {log_path}, config_path: {config_path}")
    except Exception as ex:
        print(ex)

    try:
        adminUrl, clientUrl, excelPath = FileInformation.configpath_json()
        logger.info(f'adminUrl:{adminUrl}\nclientUrl:{clientUrl}\nexcelPath:{excelPath}')
    except Exception as ex:
        print(ex)

    # print(FileInformation.excelPath)


