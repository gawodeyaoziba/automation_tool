import re


def execute_functions(data):
    """
    执行#{dama_}函数内容
    Args:
        data (dict): 待处理的数据
    Returns:
        int or None: 执行函数后的数值，如果没有匹配结果则返回 None
    """
    updated_value = None  # 初始化 updated_value
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str) and "#{" in value:
                function_names = re.findall(r'\#\{(.+?)\}', value)  # 非贪婪匹配获取所有满足条件的函数名
                for function_name in function_names:
                    if function_name.startswith("dama_"):
                        try:
                            matches = re.findall(r'([\d.]+)\#\{dama_(\d+)\}', value)  # 提取数值和替换值
                            for match in matches:
                                number_before_hash = float(match[0])  # 获取#前面的数值
                                replacement = int(match[1])  # 获取替换值
                                updated_value = number_before_hash + replacement  # 将数值和替换值相加
                        except ValueError:
                            # 如果无法将数值或替换值转换为浮点数或整数，则保持原样
                            print('请输入数字')

    if updated_value is not None:
        # 替换所有匹配到的占位符
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = re.sub(r'([\d.]+)\#\{dama_(\d+)\}', str(updated_value), value)

    return data


updated_data = {
    "用例编号": 4.0,
    "用例名称": "user_info",
    "断言内容": "{\n    \"assertType\": \"or\", \n    \"assertList\": [\n        {\n            \"key\": \"40.0#{dama_5}\", \n            \"value\": \"${bet_target}\", \n            \"type\": \"==\", \n            \"from\": \"responseBody\"\n        }\n    ]\n}"
}

result = execute_functions(updated_data)
print(result)
