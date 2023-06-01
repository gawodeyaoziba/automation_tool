import requests


class ParameterReplacer:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def replace_parameters(self, body, params, data):
        for param in params:
            param_name = param["paramName"]
            param_value = self.get_param_value(param["paramsEq"], data)
            if param_value is not None:
                body = body.replace("${" + param_name + "}", str(param_value))
        return body

    def get_param_value(self, expression, data):
        try:
            parts = expression.split('.')
            value = data
            for part in parts:
                if '[' in part:
                    key, index = part.split('[')
                    index = int(index.strip(']'))
                    value = value[key][index]
                else:
                    value = value[part]
            return value
        except (KeyError, IndexError, TypeError):
            return None


# def ces():
#     base_url = 'https://phlwin-api.pre-release.xyz'
#     endpoint = '/user/login'
#
#     """Request body"""
#     data_list = [
#         {'grecaptcha_token': '13123', 'account': 'ceshi_zdhxm_exel_a1_b3_bgw@b3.com', 'password': '12345678'},
#         {'grecaptcha_token': '0000', 'account': '${account}', 'password': '12345678'},
#         {'grecaptcha_token': '1111', 'account': '${account}', 'password': '12345678'},
#     ]
#
#     parameterize = ['是', '否']
#     parameter_data = [
#         [
#             {
#                 "paramName": "token",
#                 "paramFrom": "requestBody",
#                 "paramsEq": "data.token"
#             },
#             {
#                 "paramName": "account",
#                 "paramFrom": "requestBody",
#                 "paramsEq": "data.user.account"
#             }
#         ],
#         None
#     ]
#
#     headers_list = [
#         {'aaa': '${token}'},
#         {'aaa': '${account}'}
#     ]
#
#     replacer = ParameterReplacer()  # 创建 ParameterReplacer 实例
#
#     for index, data in enumerate(data_list):
#         request = requests.post(url=base_url + endpoint, json=data)
#         response_data = request.json()  # 获取请求返回的数据
#         print(response_data)
#         print(data)
#
#         for i, paramize in enumerate(parameterize):
#             if paramize == '是':
#                 if parameter_data[i] is not None:
#                     if index == 0:
#                         # 第一次循环时，对 data 进行参数替换
#                         data = replacer.replace_parameters(str(data_list[index]), parameter_data[i], response_data)
#                         print(data)
#                     headers = headers_list[index]
#                     # 对 headers 进行参数替换
#                     headers = replacer.replace_parameters(str(headers), parameter_data[i], response_data)
#                     print(headers)
#
#
#
# if __name__ == '__main__':
#     ces()