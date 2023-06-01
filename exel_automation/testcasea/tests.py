
import json
import requests
import logging
# import ast
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


import json
import re
import pytest
import requests

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

# ParameterReplacer 类的修改
class ParameterReplacer:
    @staticmethod
    def replace_parameters(body, parameterize, parameter_data, response_content):
        if parameterize == '是':
            parameter_data = json.loads(parameter_data)
            body = ParameterReplacer._replace_parameter_values(body, parameter_data, response_content)
        else:
            body = ParameterReplacer._replace_variable_values(body, response_content)
        return body

    @staticmethod
    def _replace_parameter_values(body, parameter_data, response_content):
        if isinstance(body, str):
            body_str = body
        else:
            body_str = json.dumps(body)

        for param in parameter_data:
            param_name = param["paramName"]
            param_value = ParameterReplacer._get_param_value(param["paramsEq"], response_content)
            if param_value is not None:
                pattern = r"\${" + re.escape(param_name) + r"}"  # 移除边界 \b
                body_str = re.sub(pattern, str(param_value), body_str)

        if isinstance(body, str):
            return body_str
        else:
            return json.loads(body_str)

    @staticmethod
    def _replace_variable_values(body, response_content):
        if isinstance(body, str):
            body_str = body
        else:
            body_str = json.dumps(body)

        def replace_variable(match):
            variable = match.group(1)
            value = ParameterReplacer._get_param_value(variable, response_content)
            return str(value) if value is not None else match.group()

        body_str = re.sub(r"\${(.*?)}", replace_variable, body_str)

        if isinstance(body, str):
            return body_str
        else:
            return json.loads(body_str)

    @staticmethod
    def _replace_expression_values(body, response_content):
        if isinstance(body, str):
            body_str = body
        else:
            body_str = json.dumps(body)

        def replace_expression(match):
            expression = match.group(1)
            value = ParameterReplacer._get_param_value(expression, response_content)
            return str(value) if value is not None else match.group()

        body_str = re.sub(r"\${(.*?)}", replace_expression, body_str)

        if isinstance(body, str):
            return body_str
        else:
            return json.loads(body_str)

    @staticmethod
    def _get_param_value(expression, data):
        try:
            parts = expression.split('.')
            value = data
            for part in parts:
                if '[' in part:
                    key, index = part.split('[')
                    index = int(index.strip(']'))
                    value = value[key][index]
                else:
                    value = value[part]
            return value
        except (KeyError, IndexError, TypeError):
            return None
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
    logger.info(f'开始执行第{test_case.case_number}用例')
    if not test_case.assertion:
        return
    logger.info(f'这是第{test_case.case_number}用例的请求体{test_case.body}')
    logger.info(f'这是他的请求头{test_case.headers}')
    logger.info(f'这是他请求的url{clientUrl + test_case.api_url}')
    logger.info(f'这是它的断言内容{test_case.assertion}')
    response_content = {}

    # 添加以下代码，用于替换参数
    if test_case.parameterize or any("${" in str(value) for value in test_case.body.values()):
        body = ParameterReplacer.replace_parameters(test_case.body, test_case.parameterize, test_case.parameter_data,
                                                    response_content)
    else:
        body = test_case.body
    body = ParameterReplacer._replace_variable_values(body, response_content)
    response = requests.request(
        method=test_case.request_method,
        url=clientUrl + test_case.api_url,
        json=body,  # 使用替换后的 body
        proxies={'https': 'http://127.0.0.1:7890'}
    )
    logger.debug(f'这是响应后的请求体{body}')
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
    logger.info(f'执行完成了这是它的响应内容{response_content}')
    logger.info(f'这是它的响应状态码{response.status_code}')
    assertion_config = json.loads(test_case.assertion)
    assert assertion_template.assertions(response_content, assertion_config)
    logger.info(f'结束执行第{test_case.case_number}用例')

def pytest_generate_tests(metafunc):
    if 'test_case' in metafunc.fixturenames:
        test_cases = get_test_cases()
        metafunc.parametrize('test_case', test_cases, ids=lambda tc: tc.case_name)

def test_execute_test_case(test_case):
    if test_case.execute == '是':
        try:
            if test_case.main_api == '是' or test_case.main_api == '否':
                execute_test_case(test_case)  # 只传递 test_case，将参数替换逻辑移到 execute_test_case 方法中
        except Exception as e:
            logger.error(f"主流程报错了所以停止了运行: {test_case.case_number}{test_case.case_name} {str(e)}")
            if test_case.main_api == str('是'):
                raise e
            else:
                print('main_api为否但是还是报告了一个错误，程序将继续执行。')
                print('错误内容：', e)
    elif test_case.execute == '否':
        logger.error(f'不执行第{test_case.case_number}{test_case.case_name}')


if __name__ == '__main__':
    pytest.main(['-vs', '--html=report.html', '--capture=no'])