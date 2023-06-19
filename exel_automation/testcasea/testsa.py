"""获取exel内容"""
from exel_automation.readexel.assets import TestExcel
testexcel = TestExcel()

"""枚举"""
from GloaEnum.GloaEnum import CONFIGURATION
from GloaEnum.GloaEnum import EXEL
from GloaEnum.GloaEnum import EXAMPLE

"""获取config.json文件"""
from exel_automation.getfile.get_assets import ConfigurationFile
ConfigurationFile = ConfigurationFile()
clientUrl = ConfigurationFile.configuration_file(CONFIGURATION.CLIENTURL.value)

"""日志"""
from log.assets import Logger
logger = Logger()

"""参数化"""
from exel_automation.to_parameterize.assets import ToParameterize
toparameterize = ToParameterize()

"""断言"""
from exel_automation.assertion_tool.assets import AssertionTemplate
assertion_template = AssertionTemplate()

"""配置"""
from exel_automation.testcasea.config import proxies

"""模块"""
import pytest
import requests
import json

class Test_case:
    test_cases = testexcel.read_file()
    test_cases = [json.loads(tc) for tc in test_cases]
    ids = [f"test_case_{tc[EXEL.CASE_NAME.value]}" for tc in test_cases]

    @pytest.mark.parametrize("test_case", test_cases, ids=ids)
    def test_case_execution(self, test_case):
        case_number = test_case.get(EXEL.CASE_NUMBER.value)
        case_name = test_case.get(EXEL.CASE_NAME.value)
        case_title = test_case.get(EXEL.CASE_TITLE.value)
        api_url = test_case.get(EXEL.API_URL.value)
        request_method = test_case.get(EXEL.REQUEST_METHOD.value)
        main_api = test_case.get(EXEL.MAIN_API.value)
        headers = test_case.get(EXEL.HEADERS.value)
        request_body = test_case.get(EXEL.BODY.value)
        execute = test_case.get(EXEL.EXECUTE.value)
        assertion = test_case.get(EXEL.ASSERTION.value)
        parameterize = test_case.get(EXEL.PARAMETERIZE.value)
        parameter_data = test_case.get(EXEL.PARAMETER_DATA.value)
        body = json.loads(request_body)
        logger.info(f'{EXAMPLE.START.value}{case_number}{case_title}')

        if not assertion:
            logger.info(f'{EXAMPLE.NULL.value}')
            logger.error(f'{EXAMPLE.NULL.value}:{assertion}')
            return

        if parameterize == EXAMPLE.YES.value and parameter_data:
            parameter_data = json.loads(parameter_data)
        else:
            parameter_data = []

        if execute == EXAMPLE.NO.value:
            logger.info(f'{EXAMPLE.OTHERWISE.value}')
            logger.info(f'{EXAMPLE.FINISH.value}')
            pytest.skip(f'{EXAMPLE.OTHERWISE.value}')
            return

        try:
            if headers is None or headers == '':
                response = requests.request(request_method, clientUrl + api_url, json=body, proxies=proxies)
                response_content = (
                    response.json()
                    if response.headers.get('content-type') == 'application/json'
                    else response.text
                )
                if isinstance(response_content, str):
                    try:
                        response_content = json.loads(response_content)
                    except json.JSONDecodeError:
                        logger.info(f'{response_content}')
                assertion_config = json.loads(assertion)
                assertion_template.assertions(response_content, assertion_config)

            else:
                response = requests.request(request_method, clientUrl + api_url, json=body, headers=headers, proxies=proxies)
                response_content = (
                    response.json()
                    if response.headers.get('content-type') == 'application/json'
                    else response.text
                )
                if isinstance(response_content, str):
                    try:
                        response_content = json.loads(response_content)
                    except json.JSONDecodeError:
                        logger.error(f'{EXAMPLE.NOJSON.value}{response_content}')
                    assertion_config = json.loads(assertion)
                    assertion_template.assertions(response_content, assertion_config)
            logger.info(f'{EXAMPLE.RESPONSE.value}{response.json()}')


            # 替换后续测试用例中的占位符
            for tc in self.test_cases:
                if tc[EXEL.CASE_NUMBER.value] > case_number:
                    replace_data = toparameterize.replace_parameters(tc, parameter_data, response.json())
                    tc.update(replace_data)

        except Exception as e:
            logger.error(f"{EXAMPLE.STOP.value}: {case_number} {case_name} {str(e)}")
            if main_api == EXAMPLE.YES.value:
                raise
            else:
                logger.info(f'{EXAMPLE.CONTINUE.value}')
                logger.debug(EXAMPLE.MISTAKE.value + str(e))

        logger.info(f'{EXAMPLE.FINISH.value}')

