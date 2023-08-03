
"""枚举"""
from GloaEnum.GloaEnum import FILEINFORMATION
from GloaEnum.GloaEnum import REPORT

"""配置文件"""
from exel_automation.getfile.assets import FileInformation
FileInformation = FileInformation()

"""日志"""
from log.assets import Logger
logger = Logger()

"""模块"""
from utils.my_third_party_modules import os, json


class Report:
    def __init__(self):
        self.apiRunTimePath = FileInformation.other_function(FILEINFORMATION.APIRUNTIMEPATH.value)
        self.delete_file()

    def delete_file(self):
        if os.path.exists(self.apiRunTimePath):
            os.remove(self.apiRunTimePath)

    def testing_report(self, case_name, state, timestart, timefinish, timeconsuming, case_title, response_data):
        apiRunTimePath = {
            REPORT.CASE_NAME.value: case_name,
            REPORT.RUN_RESULT.value: state,
            REPORT.RUN_BEGIN_TIME.value: timestart,
            REPORT.RUN_END_TIME.value: timefinish,
            REPORT.RUN_TIME.value: timeconsuming,
            REPORT.CASE_TITLE.value: case_title,
            REPORT.RESPONSE_DATA.value: response_data
        }

        with open(self.apiRunTimePath, "a") as file:
            json.dump(apiRunTimePath, file)
            file.write('\n')
            file.flush()
            file.close()
        logger.info(f"报告信息已追加到文件")









