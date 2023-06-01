"""枚举"""
from exel_automation.assertion_tool.GloaEnum import GloablEnum

"""日志"""
from exel_automation.getfile.assets import FileInformation
from log.assets import Logger
log_path, config_path = FileInformation.get_data()
logger = Logger(log_dir=log_path)


class AssertionTemplate:
    def assertions(self, request, assertion_config):
        assert_type = assertion_config.get(GloablEnum.ASSERTTYPE.value)
        assert_list = assertion_config.get(GloablEnum.ASSERTLIST.value)

        if assert_type == GloablEnum.AND.value:
            return self.process_assertion(request, assert_list[0]) and self.process_assertion(request, assert_list[1])
        elif assert_type == GloablEnum.OR.value:
            return self.process_assertion(request, assert_list[0]) or self.process_assertion(request, assert_list[1])
        elif assert_type == GloablEnum.NOT.value:
            return self.assert_not(request, assert_list)
        else:
            logger.error(GloablEnum.INVALID_ASSERTYPE.value)
            return False

    def assert_and(self, request, assert_list):
        logger.debug(f'{all(self.process_assertion(request, assertion) for assertion in assert_list)}')
        return all(self.process_assertion(request, assertion) for assertion in assert_list)

    def assert_or(self, request, assert_list):
        return any(self.process_assertion(request, assertion) for assertion in assert_list)

    def assert_not(self, request, assert_list):
        return not all(self.process_assertion(request, assertion) for assertion in assert_list)

    def process_assertion(self, request, assertion):
        assertion_from = assertion.get(GloablEnum.FROM.value)
        assertion_key = assertion.get(GloablEnum.KEY.value)
        assertion_value = assertion.get(GloablEnum.VALUE.value)
        assertion_type = assertion.get(GloablEnum.TYPE.value)

        if assertion_from == GloablEnum.RESPONSEBODY.value:
            actual_value = self.find_key_in_dict(request, assertion_key)
            return self.perform_assertion(actual_value, assertion_value, assertion_type)
        else:
            logger.error(f"{GloablEnum.ASSERT_EXCEPTION}: {assertion_from}")
            return False

    @staticmethod
    def perform_assertion(actual_value, expected_value, assertion_type):
        actual_values = str(actual_value)
        try:
            if assertion_type == GloablEnum.EQUAL.value:
                logger.debug(f'assertion_type{assertion_type}')
                if actual_values == expected_value:
                    assert_result = actual_values == expected_value
                    logger.info(f"{GloablEnum.RESPONSE.value}{actual_values}{GloablEnum.EQUAL.value}{GloablEnum.ASSERTION_VALUE.value}{expected_value}")
                    logger.info(f'{GloablEnum.ASSERTION_SUCCESS.value}')
                    logger.debug(assert_result)
                    return assert_result
                elif actual_values != expected_value:
                    logger.error(f"{GloablEnum.RESPONSE.value}{actual_values}{GloablEnum.NOTEQUALTO.value}{GloablEnum.ASSERTION_VALUE.value}{expected_value}")
                    logger.error(f'{GloablEnum.ASSERTION_FAILED.value}')
            elif assertion_type == GloablEnum.NOTEQUALTO.value:
                if actual_values != expected_value:
                    assert_result = actual_values != expected_value
                    logger.info(f"{GloablEnum.RESPONSE.value}{actual_values}{GloablEnum.NOTEQUALTO.value}{GloablEnum.ASSERTION_VALUE.value}{expected_value}")
                    logger.info(f'{GloablEnum.ASSERTION_SUCCESS.value}')
                    return assert_result
                elif actual_values == expected_value:
                    logger.error(
                        f"{GloablEnum.RESPONSE.value}{actual_values}{GloablEnum.EQUAL.value}{GloablEnum.ASSERTION_VALUE.value}{expected_value}")
                    logger.error(f'{GloablEnum.ASSERTION_FAILED.value}')
            else:
                logger.error(f"{GloablEnum.ASSERTION_FAILED.value}")
                return False
        except Exception as e:
            logger.error(f"{GloablEnum.ABNORMAL.value}{str(e)}")
    @staticmethod
    def find_key_in_dict(dictionary, key):
        if key in dictionary:
            return dictionary[key]
        for k, v in dictionary.items():
            if isinstance(v, dict):
                result = AssertionTemplate.find_key_in_dict(v, key)
                if result is not None:
                    return result
        return None
