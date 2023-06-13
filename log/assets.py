

"""枚举"""
from log.GloaEnum import GloablEnum

"""模块"""
import os
import datetime
import logging

class Logger:
    def __init__(self, log_dir=r'D:\log'):
        self.folder_path = log_dir
        self.log_folder_path = self._get_log_folder_path()

        self._setup_logging()

    def _setup_logging(self):
        # 定义日志级别和格式
        log_format = GloablEnum.LOG_FORMAT.value
        log_level = {
            GloablEnum.DEBUG.value: logging.DEBUG,
            GloablEnum.INFO.value: logging.INFO,
            GloablEnum.ERROR.value: logging.ERROR,
            GloablEnum.CRITICAL.value: logging.CRITICAL,
            GloablEnum.WARNING.value: logging.WARNING
        }

        # 设置主文件夹日志
        main_loggers = [GloablEnum.DEBUG.value,
                            GloablEnum.INFO.value,
                            GloablEnum.ERROR.value,
                            GloablEnum.CRITICAL.value,
                            GloablEnum.WARNING.value]
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
        log_folder_loggers = [GloablEnum.DEBUG.value,
                                GloablEnum.INFO.value,
                                GloablEnum.ERROR.value,
                                GloablEnum.CRITICAL.value,
                                GloablEnum.WARNING.value]
        log_folder_log_paths = [os.path.join(self.log_folder_path,
                                             f'{logger}.log') for logger in log_folder_loggers]
        for logger, log_path in zip(log_folder_loggers, log_folder_log_paths):
            logger_instance = logging.getLogger(f'{GloablEnum.LOG_FOLDER.value}{logger}')
            logger_instance.setLevel(log_level[logger])
            file_handler = logging.FileHandler(log_path, mode='a')
            file_handler.setLevel(log_level[logger])
            formatter = logging.Formatter(log_format)
            file_handler.setFormatter(formatter)
            logger_instance.addHandler(file_handler)

    def _get_log_folder_path(self):
        today = datetime.date.today().strftime(GloablEnum.YMD.value)
        log_folder = os.path.join(self.folder_path, today)
        os.makedirs(log_folder, exist_ok=True)
        return log_folder

    def create_folder_and_files(self):
        os.makedirs(self.folder_path, exist_ok=True)
        os.makedirs(self.log_folder_path, exist_ok=True)
        debug_log_path = os.path.join(self.folder_path, GloablEnum.DEBUG.value)
        info_log_path = os.path.join(self.folder_path, GloablEnum.INFO.value)
        open(debug_log_path, 'w').close()
        open(info_log_path, 'w').close()

    def debug(self, message):
        debug_logger = logging.getLogger(
            GloablEnum.DEBUG.value)
        debug_logger.debug(message)
        log_folder_debug_logger = logging.getLogger(
            GloablEnum.LOG_FOLDER_DEBUG.value)
        log_folder_debug_logger.debug(message)

    def info(self, message):
        info_logger = logging.getLogger(
            GloablEnum.INFO.value)
        info_logger.info(message)
        log_folder_info_logger = logging.getLogger(
            GloablEnum.LOG_FOLDER_INFO.value)
        log_folder_info_logger.info(message)

    def error(self, message):
        error_logger = logging.getLogger(
            GloablEnum.ERROR.value)
        error_logger.error(message)
        log_folder_error_logger = logging.getLogger(
            GloablEnum.LOG_FOLDER_ERROR.value)
        log_folder_error_logger.error(message)

    def critical(self, message):
        critical_logger = logging.getLogger(
            GloablEnum.CRITICAL.value)
        critical_logger.critical(message)
        log_folder_critical_logger = logging.getLogger(
            GloablEnum.LOG_FOLDER_CRITICAL.value)
        log_folder_critical_logger.critical(message)

    def warning(self, message):
        warning_logger = logging.getLogger(
            GloablEnum.WARNING.value)
        warning_logger.warning(message)
        log_folder_warning_logger = logging.getLogger(
            GloablEnum.LOG_FOLDER_WARNING.value)
        log_folder_warning_logger.warning(message)