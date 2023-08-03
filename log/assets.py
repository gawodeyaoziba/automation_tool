# 枚举
from GloaEnum.GloaEnum import FILEINFORMATION
from GloaEnum.GloaEnum import LOGGER
# 日志路径
from exel_automation.getfile.assets import FileInformation
# 模块
from utils.my_third_party_modules import os, datetime, logging


class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.log_dir = FileInformation().other_function(FILEINFORMATION.LOGPATH.value)
            self.folder_path = self.log_dir
            self.log_folder_path = self._get_log_folder_path()
            self._setup_logging()

    def _setup_logging(self):
        """
        设置日志记录配置
        :return:
        """
        # 定义日志级别和格式
        log_format = LOGGER.LOG_FORMAT.value
        log_level = {
            LOGGER.DEBUG.value: logging.DEBUG,
            LOGGER.INFO.value: logging.INFO,
            LOGGER.ERROR.value: logging.ERROR,
            LOGGER.CRITICAL.value: logging.CRITICAL,
            LOGGER.WARNING.value: logging.WARNING
        }

        # 设置主文件夹日志
        main_loggers = [LOGGER.DEBUG.value,
                            LOGGER.INFO.value,
                            LOGGER.ERROR.value,
                            LOGGER.CRITICAL.value,
                            LOGGER.WARNING.value]
        main_log_paths = [os.path.join(self.folder_path,
                                       f'{logger}.log') for logger in main_loggers]
        for logger, log_path in zip(main_loggers, main_log_paths):
            logger_instance = logging.getLogger(logger)
            logger_instance.setLevel(log_level[logger])
            file_handler = logging.FileHandler(log_path, mode='w')
            file_handler.setLevel(log_level[logger])
            formatter = logging.Formatter(log_format)
            file_handler.setFormatter(formatter)
            logger_instance.addHandler(file_handler)

        # 设置子文件夹日志
        log_folder_loggers = [LOGGER.DEBUG.value,
                                LOGGER.INFO.value,
                                LOGGER.ERROR.value,
                                LOGGER.CRITICAL.value,
                                LOGGER.WARNING.value]
        log_folder_log_paths = [os.path.join(self.log_folder_path,
                                             f'{logger}.log') for logger in log_folder_loggers]
        for logger, log_path in zip(log_folder_loggers, log_folder_log_paths):
            logger_instance = logging.getLogger(f'{LOGGER.LOG_FOLDER.value}{logger}')
            logger_instance.setLevel(log_level[logger])
            file_handler = logging.FileHandler(log_path, mode='a')
            file_handler.setLevel(log_level[logger])
            formatter = logging.Formatter(log_format)
            file_handler.setFormatter(formatter)
            logger_instance.addHandler(file_handler)

    def _get_log_folder_path(self):
        """
        获取今日日志文件夹路径
        """
        today = datetime.date.today().strftime(LOGGER.YMD.value)
        log_folder = os.path.join(self.folder_path, today)
        os.makedirs(log_folder, exist_ok=True)
        return log_folder

    def create_folder_and_files(self):
        """
        创建文件夹和日志文件
        """
        os.makedirs(self.folder_path, exist_ok=True)
        os.makedirs(self.log_folder_path, exist_ok=True)
        debug_log_path = os.path.join(self.folder_path, LOGGER.DEBUG.value)
        info_log_path = os.path.join(self.folder_path, LOGGER.INFO.value)
        open(debug_log_path, 'w').close()
        open(info_log_path, 'w').close()

    def debug(self, message):
        """
        记录 DEBUG 级别的日志
        """
        debug_logger = logging.getLogger(
            LOGGER.DEBUG.value)
        debug_logger.debug(message)
        log_folder_debug_logger = logging.getLogger(
            LOGGER.LOG_FOLDER_DEBUG.value)
        log_folder_debug_logger.debug(message)

    def info(self, message):
        """
        记录 INFO 级别的日志
        """
        info_logger = logging.getLogger(
            LOGGER.INFO.value)
        info_logger.info(message)
        log_folder_info_logger = logging.getLogger(
            LOGGER.LOG_FOLDER_INFO.value)
        log_folder_info_logger.info(message)

    def error(self, message):
        """
        记录 ERROR 级别的日志
        """
        error_logger = logging.getLogger(
            LOGGER.ERROR.value)
        error_logger.error(message)
        log_folder_error_logger = logging.getLogger(
            LOGGER.LOG_FOLDER_ERROR.value)
        log_folder_error_logger.error(message)

    def critical(self, message):
        """
        记录 CRITICAL 级别的日志
        """
        critical_logger = logging.getLogger(
            LOGGER.CRITICAL.value)
        critical_logger.critical(message)
        log_folder_critical_logger = logging.getLogger(
            LOGGER.LOG_FOLDER_CRITICAL.value)
        log_folder_critical_logger.critical(message)

    def warning(self, message):
        """
        记录 WARNING 级别的日志
        """
        warning_logger = logging.getLogger(
            LOGGER.WARNING.value)
        warning_logger.warning(message)
        log_folder_warning_logger = logging.getLogger(
            LOGGER.LOG_FOLDER_WARNING.value)
        log_folder_warning_logger.warning(message)
