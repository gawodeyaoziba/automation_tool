
from exel_automation.assertion_tool.assets import AssertionTemplate
# 测试代码
assertion_template = AssertionTemplate()

request = {
    'code': 200,
    'data': {
        'token': '759dccddd76e4588866d19b42ab26814',
        'user': {
            '_id': '646c746ae05c24857a63150c',
            'account': 'ceshi_zdhxm_exel_a1_b3_bgw@b3.com',
            'activities': {},
            'avatar': None,
            'balance_map': {
                'PHP': {
                    'amount': 0,
                    'bet_progress': 0,
                    'bet_target': 0,
                    'currency': 'PHP',
                    'withdrawable_amount': 0
                }
            },
            # Rest of the user data...
        }
    },
    'msg': 'OK',
    'message': 'OK'
}


assertion_config = {
    "assertType": "or", # and  or  not 都可以使用
    "assertList": [{
        "key": "_id",
        "value": "646c746ae05c24857a63150c",
        "type": "==",
        'from': 'responseBody'
    },
        {
        "key": "token",
        "value": "759dccddd76e4588866d19b42ab26814423432",
        "type": "!=",
        'from': 'responseBody'
    },
        {
            "key": "token",
            "value": "759dccddd76e4588866d19b42ab26814",
            "type": "==",
            'from': 'responseBody'
        }
    ]
}

# Call the assertions method
result = assertion_template.assertions(request, assertion_config)
print(result)









"""
1. 给予对象ID
    必填【异常捕获】
        1.每个接口唯一标识
2. 封装URL全局变量
    必填【异常捕获】
        1.B端
        2.C端
3. 封装请求方式：
    必填【异常捕获】
        1.get==get请求方式则直接请求
        2.post==post请求方式必填body
        3.put==put请求
        4.patch==patch请求方式必填body
        5.delete
        6.optlons
        7.head==head请求方式则直接请求
        8.connect
4. 封装请求头
    1.选填
        如果需要使用请求头加入数据
            必填json格式【异常捕获】
        如果不需要使用请求头，则请求时不输入请求头
5. 封装请求体
6. 封装响应体
7. 封装状态码
8. 封装参数化
    1.
9. 封装日志内容
    1.每天生成对应文件夹日志内容
        1.debug==最低级别，追踪问题时使用
        2.error==用于记录程序报错信息
        3.info==记录程序中一般事件的信息，或确认一切工作正常
        4.warning==记录信息，用于警告
        5.critical==最高级别，记录可能导致程序崩溃的错误
"""