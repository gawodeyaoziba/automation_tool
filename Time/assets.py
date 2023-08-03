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





import time
from datetime import datetime

# 定义一个装饰器函数
def calculate_time(func):
    def wrapper(*args, **kwargs):
        # 记录函数开始时间
        start_time = time.time()

        # 执行原函数
        result = func(*args, **kwargs)

        # 计算函数执行时间
        end_time = time.time()
        execution_time = end_time - start_time

        # 格式化时间输出
        execution_time_seconds = int(execution_time)
        execution_time_milliseconds = int((execution_time - execution_time_seconds) * 1000)
        execution_time_formatted = datetime.fromtimestamp(end_time).strftime("%Y年%m月%d日，%H时%M分%S秒")

        print(f"执行时间为：{execution_time_formatted}，耗时时间为：{execution_time_milliseconds} 毫秒")

        return result

    return wrapper



