"""模块"""
import xlrd

"""枚举"""
from GloaEnum.GloaEnum import EXEL
from GloaEnum.GloaEnum import CONFIGURATION
"""路径"""
from exel_automation.getfile.get_assets import ConfigurationFile
ConfigurationFile = ConfigurationFile()
"""模块"""
import json

"""日志"""
from log.assets import Logger

"""获取exel内容"""
class TestExcel:
    def __init__(self):
        self.logger = Logger()
        self.excelPath = ConfigurationFile.configuration_file(CONFIGURATION.EXECELPATH.value)

    def read_file(self, sheet_index=0, row_index=1):
        self.logger.info(f'{EXEL.START_EXCEL.value}')
        workbook = xlrd.open_workbook(self.excelPath)
        sheet = workbook.sheet_by_index(sheet_index)
        header = sheet.row_values(0)
        result = []
        for row in range(row_index, sheet.nrows):
            row_data = sheet.row_values(row)
            js_object = {}
            for i in range(len(header)):
                js_object[header[i]] = row_data[i]

            js_string = json.dumps(js_object, ensure_ascii=False)
            self.logger.debug(f'{EXEL.LINE.value}{row}{EXEL.LINE_OLL.value}{js_object}')
            result.append(js_string)
        self.logger.info(f'{EXEL.OVER.value}')
        return result





