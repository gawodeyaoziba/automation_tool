from enum import Enum

class LOGGER(Enum):
    """日志级别"""
    DEBUG = 'debug'                 # debug
    INFO = 'info'                   # info
    ERROR = 'error'                 # error
    CRITICAL = 'critical'           # critical
    WARNING = 'warning'             # warning
    LOG_LEVELS = ['DEBUG', 'INFO', 'ERROR', 'CRITICAL', 'WARNING']

    """日志格式"""
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    YMD = '%Y-%m-%d'

    """子文件日志"""
    LOG_FOLDER = 'log_folder_'
    LOG_FOLDER_DEBUG = 'log_folder_debug'
    LOG_FOLDER_INFO = 'log_folder_info'
    LOG_FOLDER_ERROR = 'log_folder_error'
    LOG_FOLDER_CRITICAL = 'log_folder_critical'
    LOG_FOLDER_WARNING = 'log_folder_warning'

"""配置文件"""
class FILEINFORMATION(Enum):
    """配置文件内容"""
    PYTHONPROJECTPATH = 'pythonProjectPath'  # 自动化文件路劲
    LOGPATH = 'logPath'  # 日志文件路径
    REPORTPATH = 'reportPath'  # 测试报告路径
    CONFIGPATH = 'configPath'  # 配置文件路径
    APIRUNTIMEPATH = 'apiRunTimePath'  # 测试结果路径


"""configuration配置文件"""
class CONFIGURATION(Enum):
    """json配置文件"""
    ADMINURL = 'adminUrl'  # C端全局url
    CLIENTURL = 'clientUrl'  # B端全局url
    EXECELPATH = 'excelPath'  # exel文件路径
    CURRENT = 'current'  # 币种
    THREADNUM = 'threadNum'  # id


"""exel"""
class EXEL(Enum):
    """exel头部内容"""
    CASE_NUMBER = '用例编号'               # case_number
    CASE_NAME = "用例名称"                   # case_name
    CASE_TITLE = "用例标题"                 # case_title
    API_URL = "接口地址"                       # api_url
    REQUEST_METHOD = "请求方式"         # request_method
    MAIN_API = "主流程api"                     # main_api
    HEADERS = "请求头"                       # headers
    BODY = "请求体"                             # body
    EXECUTE = "是否执行"                       # execute
    ASSERTION = "断言内容"                   # assertion
    PARAMETERIZE = "是否参数化"             # parameterize
    PARAMETER_DATA = "参数化数据"         # parameter_data

    """exel状态"""
    START_EXCEL= '开始获取excel文件内容'
    LINE = '这是excel文件第'
    LINE_OLL = '行内容的详细信息: '
    OVER = '获取excel文件内容结束'

"""断言"""
class ASSERTION(Enum):
    ASSERTTYPE = 'assertType'  # 断言类型
    ASSERTLIST = 'assertList'  # 断言列表
    RESPONSEBODY = 'responseBody'  # 响应体
    AND = 'and'  # 与
    OR = 'or'  # 或
    NOT = 'not'  # 非
    EQUAL = '=='  # 等于
    NOTEQUALTO = '!='  # 不等于

    """编写值"""
    FROM = 'from'  # 获取的路径
    KEY = 'key'  # 值
    VALUE = 'value'  # 判断值
    TYPE = 'type'  # 判断类型

    """日志"""
    INVALID_ASSERTYPE = '无效的断言类型'  # 无效的断言类型
    ASSERT_EXCEPTION = '断言获取内容写入异常'  # 断言获取内容写入异常
    RESPONSE = '响应值:'  # 响应值
    ASSERTION_VALUE = '断言值'  # 断言值
    ASSERTION_FAILED = '断言失败'  # 断言失败
    ASSERTION_SUCCESS = '断言成功'  # 断言成功
    ABNORMAL = '断言内容异常，请查看输入的断言值'

class EXAMPLE(Enum):
    START = '开始执行用例'
    NULL = '断言内容不能为空'
    YES = '是'
    NO = '否'
    NOJSON = '这是原始响应内容（不是 JSON）'
    FINISH = '执行用例结束'
    MISTAKE = '错误内容 : '
    CONTINUE = '主流程为否但是还是报告了一个错误，程序将继续执行'
    STOP = '主流程报错了所以停止了运行'
    RESPONSE = '这是响应的内容'
    OTHERWISE= '此用例执行为否，不执行此用例'