
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