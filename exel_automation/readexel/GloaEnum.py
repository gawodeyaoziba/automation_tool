from enum import Enum

class GloablEnum(Enum):
    CASE_NUMBER = 'case_number'               # 用例编号
    CASE_NAME = "case_name"                   # 用例名称
    CASE_TITLE = "case_title"                 # 用例标题
    API_URL = "api_url"                       # 接口地址
    REQUEST_METHOD = "request_method"         # 请求方式
    MAIN_API = "main_api"                     # 主流程api
    HEADERS = "headers"                       # 请求头
    BODY = "body"                             # 请求体
    EXECUTE = "execute"                       # 是否执行
    ASSERTION = "assertion"                   # 断言内容
    PARAMETERIZE = "parameterize"             # 是否参数化
    PARAMETER_DATA = "parameter_data"         # 参数化数据


    """
    日志内容
    """
    EXEL_ROW_INDEX = "line use case content"        # 行用例内容