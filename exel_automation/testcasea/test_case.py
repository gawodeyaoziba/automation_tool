"""枚举"""
from GloaEnum.GloaEnum import EXAMPLE
from GloaEnum.GloaEnum import EXEL
"""时间"""
from Time.assets import Time
timestart = Time()

"""断言"""
from exel_automation.assertion_tool.assets import AssertionTemplate
assertion_template = AssertionTemplate()

"""日志"""
from log.assets import Logger
logger = Logger()

"""生成测试报告"""
from exel_automation.testcasea.Report.Report import Report
Report = Report()
"""代理"""
from Clash_yaml.assets import ClashProxyHandler
ClashProxyHandler = ClashProxyHandler()

"""模块"""
import time
import json
import requests
import urllib.request
proxies = urllib.request.getproxies()
"""接口请求方式单独封装处理"""
class Implement:




    def no_headers(self, case_number, request_method, url, body, headers, assertion, case_name, case_title):
        timestar = timestart.get_now_datetime()

        start = int(time.time() * 1000)
        start_time = round(start, 2)
        logger.debug(f'{case_title}{EXEL.HEADERS.value}:{case_number}{headers}')
        logger.debug(f'{case_title}{EXEL.BODY.value}:{case_number}{body}')
        logger.debug(f'{case_title}{EXEL.URL.value}:{case_number}{url}')
        logger.debug(f'{case_title}{EXEL.ASSERTION.value}:{case_number}{assertion}')
        response = requests.request(request_method, url, json=body, proxies=ClashProxyHandler.get_proxies())
        assertion_config = json.loads(assertion)
        try:
            assertion_template.assertions(response.json(), assertion_config)
            state = True
        except Exception as e:
            state = False

        Finish = int(time.time() * 1000)
        Finish_time = round(Finish, 2)

        timefinish = timestart.get_now_datetime()

        Report.testing_report(case_name, state, timestar, timefinish, Finish_time - start_time)

        logger.info(f'{EXAMPLE.RESPONSE.value}{response.json()}')
        return response.json()

    def yes_headers(self, headers, request_method, url, body, assertion, case_name, case_title, case_number):
        headers_dict = json.loads(headers)

        timestar = timestart.get_now_datetime()
        start = int(time.time() * 1000)
        start_time = round(start, 2)

        logger.debug(f'{case_title}{EXEL.HEADERS.value}:{case_number}{headers}')
        logger.debug(f'{case_title}{EXEL.BODY.value}:{case_number}{body}')
        logger.debug(f'{case_title}{EXEL.URL.value}:{case_number}{url}')
        logger.debug(f'{case_title}{EXEL.ASSERTION.value}:{case_number}{assertion}')

        response = requests.request(request_method, url, json=body, headers=headers_dict, proxies=ClashProxyHandler.get_proxies())
        assertion_config = json.loads(assertion)
        try:
            assertion_template.assertions(response.json(), assertion_config)
            state = True
        except Exception as e:
            state = False
        Finish = int(time.time() * 1000)
        Finish_time = round(Finish, 2)

        timefinish = timestart.get_now_datetime()
        Report.testing_report(case_name, state, timestar, timefinish, Finish_time - start_time)
        return response.json()