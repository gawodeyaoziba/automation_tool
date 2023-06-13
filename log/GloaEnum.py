from enum import Enum

class GloablEnum(Enum):

    """日志级别"""
    DEBUG = 'debug'                 # debug
    INFO = 'info'                   # info
    ERROR = 'error'                 # error
    CRITICAL = 'critical'           # critical
    WARNING = 'warning'             # warning

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