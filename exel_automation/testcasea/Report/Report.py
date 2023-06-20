
"""枚举"""
from GloaEnum.GloaEnum import FILEINFORMATION

"""配置文件"""
from exel_automation.getfile.assets import FileInformation
FileInformation = FileInformation()

"""日志"""
from log.assets import Logger
logger = Logger()



x = [{
    "case_name": "register_user",
    "run_result": "true",
    "run_begin_time": "2023-05-28 10:17:15,412",
    "run_end_time": "2023-05-28 10:17:15,720",
    "run_time": 608
},
{
    "case_name": "login_user",
    "run_result": "true",
    "run_begin_time": "2023-05-28 10:21:15,412",
    "run_end_time": "2023-05-28 10:21:15,620",
    "run_time": 504
}]
"""模块"""
import json
import json


class Report:
    def __init__(self):
        self.apiRunTimePath = FileInformation.other_function(FILEINFORMATION.APIRUNTIMEPATH.value)

    def testing_report(self, case_name, state, timestart, timefinish, timeconsuming):
        apiRunTimePath = {
            "case_name": case_name,
            "run_result": state,
            "run_begin_time": timestart,
            "run_end_time": timefinish,
            "run_time": timeconsuming
        }
        filename = self.apiRunTimePath

        with open(filename, "a") as file:
            json.dump(apiRunTimePath, file)
            file.write('\n')

        logger.info(f"报告信息已追加到文件 '{filename}'")







