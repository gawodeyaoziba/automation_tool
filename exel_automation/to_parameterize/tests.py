import pytest
import openpyxl
import re


def get_test_data():
    wb = openpyxl.load_workbook('test_data.xlsx')
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    return data[1:]  # Skip the header row


def replace_parameters(data, parameters):
    replaced_data = {}
    for key, value in data.items():
        replaced_value = value
        for param in parameters:
            param_name = '${' + param + '}'
            if param_name in replaced_value:
                replaced_value = replaced_value.replace(param_name, parameters[param])
        replaced_data[key] = replaced_value
    return replaced_data


@pytest.mark.parametrize('case_id, url, method, body', get_test_data())
def test_example(case_id, url, method, body):
    # 根据具体需求编写测试逻辑
    print(f'Running test case {case_id}')
    print(f'URL: {url}')
    print(f'Method: {method}')
    print(f'Original Body: {body}')

    # 参数替换处理
    parameter_regex = r'\${([^}]+)}'
    parameters = re.findall(parameter_regex, body)
    replacements = {'password': 'pass123'}  # 根据具体参数替换需求进行设置
    replaced_body = replace_parameters(body, replacements)
    print(f'Replaced Body: {replaced_body}')

    # 在这里可以继续编写测试逻辑，使用替换后的请求体进行请求


# 执行测试
pytest.main(['test_example.py'])
