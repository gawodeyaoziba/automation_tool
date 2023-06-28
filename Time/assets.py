import time

class Time:
    def get_now_datetime(self):
        """
        @Description: 返回当前时间，格式为：年月日时分秒
        """
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        return now

    def get_now_time(self):
        """
        @Description: 返回当前时间，格式为：时分秒
        """
        now = time.strftime('%H-%M-%S')
        return now

    def get_now_date(self):
        """
        @Description: 返回当前时间，格式为：年月日
        """
        now = time.strftime('%Y-%m-%d')
        return now


