from enum import Enum

class GloablEnum(Enum):
    DATA = "data"                           # data字段
    LOGPATH = 'logPath'                     # 获取日志文件路径
    CONFIGPATH = 'configPath'               # 获取配置文件路径
    DEFAULT_LOG_PATH = 'default_log_path'   # 设置默认日志路径
    ADMINURL = 'adminUrl'                   # C端全局变量url
    CLIENTURL = 'clientUrl'                 # B端全局变量url
    EXECELPATH = 'excelPath'                # 获取exel文件路径



    """文件操作"""
    R = 'r'                                 # 打开文件

    """
    日志信息
    """
    GET_DATA_ERROR_MSG = 'Did not get configuration information'            # 没有获取到配置信息
    CONFIGPATH_JSON_PRINT = 'Unable to retrieve configuration file path'    # 无法检索配置文件路径
    CONFIGPATH_JSON_ERROR_MSG = "Did not get configuration file path"       # 没有获取到配置文件路径
    CONFIGPATH_JSON_LOGGER = 'This is the configpath_json file content'     # 这是configpath_json文件内容
