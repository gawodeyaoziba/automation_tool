"""
需求：
模块：xlrd
读取exel文件
对exel文件里第二行的内容进行封装，并复用此对象【注：第二行，第三行也可使用此对象】每行有12个对象
下面是对象的名称：
    self.case_number = ""
    self.case_name = ""
    self.case_title = ""
    self.api_url =""
    self.request_method = ""
    self.main_api = ""
    self.headers =""
    self.body = ""
    self.execute = ""
    self.assertion = ""
    self.parameterize = ""
    self.parameter_data = ""
文件路劲：
    'D:\\api-auto-test.xls'
"""
from exel_automation.readexel.assets import ExcelFileReader



if __name__ == '__main__':
    reader = ExcelFileReader()
    test_cases = reader.read_file(sheet_index=0, start_row=1)
    print(test_cases)
    for test_case in test_cases:
        print(test_case.__dict__)
        print(test_case.__dict__["case_number"])

