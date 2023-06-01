import json
import requests
import logging
import pytest

"""枚举"""
from exel_automation.readexel.GloaEnum import GloablEnum
"""Exel表格"""
from exel_automation.readexel.assets import ExcelFileReader

"""断言"""
from exel_automation.assertion_tool.assets import AssertionTemplate
assertion_template = AssertionTemplate()
"""参数化"""
# from exel_automation.to_parameterize.assets import ParameterReplacer
# replacer = ParameterReplacer()
"""日志"""
from exel_automation.getfile.assets import FileInformation
from log.assets import Logger

log_path, config_path = FileInformation.get_data()
logger = Logger(log_dir=log_path)
adminUrl, clientUrl, excelPath = FileInformation.configpath_json()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

import pytest

class TestCase:
    def __init__(self, case_number, case_name, case_title, api_url, request_method, main_api, headers, body, execute, assertion, parameterize, parameter_data):
        self.case_number = case_number
        self.case_name = case_name
        self.case_title = case_title
        self.api_url = api_url
        self.request_method = request_method
        self.main_api = main_api
        self.headers = headers
        self.body = body
        self.execute = execute
        self.assertion = assertion
        self.parameterize = parameterize
        self.parameter_data = parameter_data

def get_test_cases():
    excel_file_reader = ExcelFileReader()
    data = excel_file_reader.read_file(sheet_index=0, start_row=1)
    return [
        TestCase(
            test_case.__dict__[GloablEnum.CASE_NUMBER.value],
            test_case.__dict__[GloablEnum.CASE_NAME.value],
            test_case.__dict__[GloablEnum.CASE_TITLE.value],
            test_case.__dict__[GloablEnum.API_URL.value],
            test_case.__dict__[GloablEnum.REQUEST_METHOD.value],
            test_case.__dict__[GloablEnum.MAIN_API.value],
            test_case.__dict__[GloablEnum.HEADERS.value],
            json.loads(test_case.__dict__[GloablEnum.BODY.value]),
            test_case.__dict__[GloablEnum.EXECUTE.value],
            test_case.__dict__[GloablEnum.ASSERTION.value],
            test_case.__dict__[GloablEnum.PARAMETERIZE.value],
            test_case.__dict__[GloablEnum.PARAMETER_DATA.value]
        )
        for test_case in data
    ]

def execute_test_case(test_case):
    try:
        logger.info(f'开始执行第{test_case.case_number}用例')
        logger.info(f'这是第{test_case.case_number}用例的请求体：{test_case.body}')
        logger.info(f'这是他的请求头：{test_case.headers}')
        logger.info(f'这是他请求的url：{clientUrl + test_case.api_url}')
        logger.info(f'这是它的断言内容：{test_case.assertion}')
        if not test_case.assertion:
            logger.info(f'跳过此时用例，断言内容不能为空')
            logger.error(f'断言内容不能为空：{test_case.assertion}')
            return
        response_content = {}
        response = requests.request(
            method=test_case.request_method,
            url=clientUrl + test_case.api_url,
            json=test_case.body,
            proxies={'https': 'http://127.0.0.1:7890'}
        )
        response_content = (
            response.json()
            if response.headers.get('content-type') == 'application/json'
            else response.text
        )
        if isinstance(response_content, str):
            try:
                response_content = json.loads(response_content)
            except json.JSONDecodeError:
                print(f'This is the raw response content (not JSON): {response_content}')
        logger.info(f'执行完成了这是它的响应内容：{response_content}')
        logger.info(f'这是它的响应状态码：{response.status_code}')

        assertion_config = json.loads(test_case.assertion)
        assertion_template.assertions(response_content, assertion_config)

        logger.info(f'结束执行第{test_case.case_number}用例')
    except Exception as e:
        logger.error(f'程序异常报错了{str(e)}')


def pytest_generate_tests(metafunc):
    if 'test_case' in metafunc.fixturenames:
        test_cases = get_test_cases()
        metafunc.parametrize('test_case', test_cases, ids=lambda tc: tc.case_name)

def test_execute_test_case(test_case):
    if test_case.execute == '是':
        try:
            if test_case.main_api == str('是'):
                execute_test_case(test_case)
            elif test_case.main_api == '否':
                execute_test_case(test_case)
        except Exception as e:
            logger.error(f"主流程报错了所以停止了运行: {test_case.case_number}{test_case.case_name} {str(e)}")
            if test_case.main_api == str('是'):
                raise e
            else:
                print('main_api为否但是还是报告了一个错误，程序将继续执行。')
                print('错误内容：', e)
    elif test_case.execute == '否':
        logger.info(f'不执行第{test_case.case_number}{test_case.case_name}因为execute={test_case.execute}')

if __name__ == '__main__':
    pytest.main(['-vs', '--html=report.html', '--capture=no'])


