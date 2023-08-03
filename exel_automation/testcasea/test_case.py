"""枚举"""
from GloaEnum.GloaEnum import EXAMPLE
from GloaEnum.GloaEnum import EXEL
"""时间"""
from Time.assets import Time
timestart = Time()

"""断言"""
from utils.assertion import AssertionTemplate
assertion_template = AssertionTemplate()

"""日志"""
from log.assets import Logger
logger = Logger()

"""生成测试报告"""
from exel_automation.testcasea.Report.Report import Report
Report = Report()
"""代理"""
from exel_automation.testcasea.config import proxies

"""模块"""
from utils.my_third_party_modules import time, json, requests



"""接口请求方式单独封装处理"""
class Implement:
    def post_no_headers(self, case_number, request_method, url, body, headers, assertion, case_name, case_title):
        timestar = timestart.get_now_datetime()

        start = int(time.time() * 1000)
        start_time = round(start, 2)
        logger.debug(f'{case_title}{EXEL.HEADERS.value}:{case_number}{headers}')
        logger.debug(f'{case_title}{EXEL.BODY.value}:{case_number}{body}')
        logger.debug(f'{case_title}{EXEL.URL.value}:{case_number}{url}')
        logger.debug(f'{case_title}{EXEL.ASSERTION.value}:{case_number}{assertion}')
        print("aaaa", request_method)
        response = requests.request(request_method, url, json=body, proxies=proxies)
        assertion_config = json.loads(assertion)
        try:
            assertion_template.assertions(response.json(), assertion_config)
            state = True
        except Exception as e:
            state = False

        Finish = int(time.time() * 1000)
        Finish_time = round(Finish, 2)

        timefinish = timestart.get_now_datetime()


        Report.testing_report(case_name, state, timestar, timefinish, Finish_time - start_time, case_title, response.json())

        logger.info(f'{EXAMPLE.RESPONSE.value}{response.json()}')
        return response.json()

    def post_yes_headers(self, headers, request_method, url, body, assertion, case_name, case_title, case_number):
        headers_dict = json.loads(headers)

        timestar = timestart.get_now_datetime()
        start = int(time.time() * 1000)
        start_time = round(start, 2)

        logger.debug(f'{case_title}{EXEL.HEADERS.value}:{case_number}{headers}')
        logger.debug(f'{case_title}{EXEL.BODY.value}:{case_number}{body}')
        logger.debug(f'{case_title}{EXEL.URL.value}:{case_number}{url}')
        logger.debug(f'{case_title}{EXEL.ASSERTION.value}:{case_number}{assertion}')

        response = requests.request(request_method, url, json=body, headers=headers_dict, proxies=proxies)
        assertion_config = json.loads(assertion)
        try:
            assertion_template.assertions(response.json(), assertion_config)
            state = True
        except Exception as e:
            state = False
        Finish = int(time.time() * 1000)
        Finish_time = round(Finish, 2)

        timefinish = timestart.get_now_datetime()
        Report.testing_report(case_name, state, timestar, timefinish, Finish_time - start_time, case_title, response.json())
        return response.json()
