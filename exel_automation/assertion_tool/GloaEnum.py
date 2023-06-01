from enum import Enum

class GloablEnum(Enum):
    ASSERTTYPE = 'assertType'       # 断言类型
    ASSERTLIST = 'assertList'       # 断言列表
    RESPONSEBODY = 'responseBody'   # 响应体
    AND = 'and'                     # 与
    OR = 'or'                       # 或
    NOT = 'not'                     # 非
    EQUAL = '=='                    # 等于
    NOTEQUALTO = '!='               # 不等于


    """编写值"""
    FROM = 'from'                   # 获取的路径
    KEY = 'key'                     # 值
    VALUE = 'value'                 # 判断值
    TYPE = 'type'                   # 判断类型




    """日志"""
    INVALID_ASSERTYPE = '无效的断言类型'                               # 无效的断言类型
    ASSERT_EXCEPTION = '断言获取内容写入异常'                           # 断言获取内容写入异常
    RESPONSE = '响应值:'                                             # 响应值
    ASSERTION_VALUE = '断言值'                                       # 断言值
    ASSERTION_FAILED = '断言失败'                                    # 断言失败
    ASSERTION_SUCCESS = '断言成功'                                   # 断言成功
    ABNORMAL = '断言内容异常，请查看输入的断言值'
