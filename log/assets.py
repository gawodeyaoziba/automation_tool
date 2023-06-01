import logging
import os
import datetime

class Logger:
    def __init__(self, log_dir='D:/log', overwrite_logs=False):
        self.log_dir = log_dir
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.overwrite_logs = overwrite_logs

        # Check if log directory exists, create it if not
        os.makedirs(log_dir, exist_ok=True)

        self.log_folder = None
        self.file_handlers = {}

    def _get_log_folder_path(self):
        today = datetime.date.today().strftime('%Y-%m-%d')
        log_folder = os.path.join(self.log_dir, f'{today}log')
        os.makedirs(log_folder, exist_ok=True)
        return log_folder

    def _create_file_handler(self, log_level, mode):
        log_folder = self._get_log_folder_path()
        log_file = os.path.join(log_folder, f'{log_level}.log')
        file_handler = logging.FileHandler(log_file, mode=mode)
        file_handler.setLevel(logging.getLevelName(log_level.upper()))
        file_handler.setFormatter(self.formatter)
        return file_handler

    def _create_overwrite_file_handler(self, log_level):
        return self._create_file_handler(log_level, mode='w')

    def _get_or_create_file_handler(self, log_level):
        if self.log_folder is None or self.log_folder != self._get_log_folder_path():
            self.log_folder = self._get_log_folder_path()
            self.file_handlers.clear()

        if log_level not in self.file_handlers:
            if self.overwrite_logs:
                file_handler = self._create_overwrite_file_handler(log_level)
            else:
                file_handler = self._create_file_handler(log_level, mode='a')
            self.file_handlers[log_level] = file_handler

        return self.file_handlers[log_level]

    def _get_or_create_overwrite_file_handler(self, log_level):
        if self.log_folder is None or self.log_folder != self._get_log_folder_path():
            self.log_folder = self._get_log_folder_path()
            self.file_handlers.clear()

        if log_level not in self.file_handlers:
            file_handler = self._create_overwrite_file_handler(log_level)
            self.file_handlers[log_level] = file_handler

        return self.file_handlers[log_level]

    def debug(self, msg):
        if self.overwrite_logs:
            file_handler = self._get_or_create_overwrite_file_handler('debug')
        else:
            file_handler = self._get_or_create_file_handler('debug')
        self.logger.addHandler(file_handler)
        self.logger.debug(msg)
        self.logger.removeHandler(file_handler)

    def info(self, msg):
        if self.overwrite_logs:
            file_handler = self._get_or_create_overwrite_file_handler('info')
        else:
            file_handler = self._get_or_create_file_handler('info')
        self.logger.addHandler(file_handler)
        self.logger.info(msg)
        self.logger.removeHandler(file_handler)

    def error(self, msg):
        if self.overwrite_logs:
            file_handler = self._get_or_create_overwrite_file_handler('error')
        else:
            file_handler = self._get_or_create_file_handler('error')
        self.logger.addHandler(file_handler)
        self.logger.error(msg)
        self.logger.removeHandler(file_handler)

    def critical(self, msg):
        if self.overwrite_logs:
            file_handler = self._get_or_create_overwrite_file_handler('critical')
        else:
            file_handler = self._get_or_create_file_handler('critical')
        self.logger.addHandler(file_handler)
        self.logger.critical(msg)
        self.logger.removeHandler(file_handler)


    def warning(self, msg):
        if self.overwrite_logs:
            file_handler = self._get_or_create_overwrite_file_handler('warning')
        else:
            file_handler = self._get_or_create_file_handler('warning')
        self.logger.addHandler(file_handler)
        self.logger.error(msg)
        self.logger.removeHandler(file_handler)

