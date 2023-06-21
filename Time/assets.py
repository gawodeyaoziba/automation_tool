"""
@Description: 获取当前时间
"""
import time
import datetime

class Time:
    def get_now_datetime(self):
        """
        @Description: 返回当前时间，格式为：年月日时分秒
        """
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    def get_now_time(self):
        """
        @Description: 返回当前时间，格式为：时分秒
        """
        return time.strftime('%H-%M-%S', time.localtime(time.time()))

    def get_now_date(self):
        """
        @Description: 返回当前时间，格式为：年月日
        """
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

