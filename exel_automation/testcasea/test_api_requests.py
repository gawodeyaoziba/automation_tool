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


"""调用接口"""
from exel_automation.testcasea.test_utils import Replace
replace = Replace()

"""模块"""
import pytest
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
        url = clientUrl + api_url
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

        replace.replace(case_number, request_method, url, body, headers, assertion, case_name, parameter_data, case_title, self.test_cases, main_api)
