"""调用接口"""
from exel_automation.testcasea.test_case import Implement
implement = Implement()
"""枚举"""
from GloaEnum.GloaEnum import EXEL
from GloaEnum.GloaEnum import EXAMPLE
"""参数化"""
from utils.parameter_substitution import ToParameterize
toparameterize = ToParameterize()
"""日志"""
from log.assets import Logger
logger = Logger()

"""进行替换参数以及调用接口"""
class Replace:
    def replace(self, case_number, request_method, url, body, headers, assertion, case_name, parameter_data, case_title, test_cases, main_api):
        try:


            if not headers:
                response = implement.post_no_headers(case_number, request_method, url, body, headers, assertion, case_name, case_title)
            else:
                response = implement.post_yes_headers(headers, request_method, url, body, assertion, case_name, case_title, case_number)

            # if request_method == 'get':
            #     response = implement.get_headers(request_method, url, assertion, case_name, case_title, case_number)

            # 替换后续测试用例中的占位符
            for tc in test_cases:
                if tc[EXEL.CASE_NUMBER.value] > case_number:
                    if isinstance(response, dict):
                        replace_data = toparameterize.replace_parameters(tc, parameter_data, response)
                        tc.update(replace_data)
                    else:
                        replace_data = toparameterize.replace_parameters(tc, parameter_data, response.json())
                        tc.update(replace_data)


        except Exception as e:
            logger.error(f"{EXAMPLE.STOP.value}: {case_number} {case_name} {str(e)}")
            if main_api == EXAMPLE.YES.value:
                raise
            else:
                logger.info(f'{EXAMPLE.CONTINUE.value}')
                logger.debug(EXAMPLE.MISTAKE.value + str(e))

        logger.info(f'{case_number}{case_title}{EXAMPLE.FINISH.value}')
