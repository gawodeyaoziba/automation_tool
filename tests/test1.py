import re
"""日志"""
from log.assets import Logger
logger = Logger()
def process_data(data):
    # 匹配 ${aaa}#{dama_1}
    def increment_match(match):
        param_name = match.group(1)
        increment = int(match.group(2))
        if param_name not in data:
            return match.group(0)
        try:
            param_value = int(data[param_name])
        except ValueError:
            logger.error(f"{param_name} is not an integer")
            return match.group(0)
        new_value = str(param_value + increment)
        return f"${{{param_name}}}#{match.group(2)}"

    # 匹配 #{dama_22}
    def constant_match(match):
        increment = int(match.group(1))
        return f"#{dama_{match.group(1)}}"

    # 匹配 ${aaa}#{dama_${bbb}}
    def nested_match(match):
        param_name = match.group(1)
        param_inner = match.group(2)
        if param_name not in data or param_inner not in data:
            return match.group(0)
        try:
            param_value = int(data[param_name])
        except ValueError:
            logger.error(f"{param_name} is not an integer")
            return match.group(0)
        try:
            inner_value = int(data[param_inner])
        except ValueError:
            logger.error(f"{param_inner} is not an integer")
            return match.group(0)
        new_value = str(param_value + inner_value)
        return f"${{{param_name}}}#{match.group(2)}"

    for key, value in data.items():
        if isinstance(value, str):
            # 匹配 ${aaa}#{dama_1}
            value = re.sub(r'\$\{([^}]+)\}#\{dama_(\d+)\}', increment_match, value)
            # 匹配 #{dama_22}
            value = re.sub(r'#\{dama_(\d+)\}', constant_match, value)
            # 匹配 ${aaa}#{dama_${bbb}}
            value = re.sub(r'\$\{([^}]+)\}#\{dama_\$\{([^}]+)\}\}', nested_match, value)
            data[key] = value

    return data
