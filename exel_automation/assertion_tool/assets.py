"""枚举"""
from GloaEnum.GloaEnum import ASSERTION

"""日志"""
from log.assets import Logger
logger = Logger()


class AssertionTemplate:
    def assertions(self, request, assertion_config):
        assert_type = assertion_config.get(ASSERTION.ASSERTTYPE.value)
        assert_list = assertion_config.get(ASSERTION.ASSERTLIST.value)

        if assert_type == ASSERTION.AND.value:
            return self.process_assertion(request, assert_list[0]) and self.process_assertion(request, assert_list[1])
        elif assert_type == ASSERTION.OR.value:
            return self.process_assertion(request, assert_list[0]) or self.process_assertion(request, assert_list[1])
        elif assert_type == ASSERTION.NOT.value:
            return self.assert_not(request, assert_list)
        else:
            logger.error(ASSERTION.INVALID_ASSERTYPE.value)
            return False

    def assert_and(self, request, assert_list):
        logger.debug(f'{all(self.process_assertion(request, assertion) for assertion in assert_list)}')
        return all(self.process_assertion(request, assertion) for assertion in assert_list)

    def assert_or(self, request, assert_list):
        return any(self.process_assertion(request, assertion) for assertion in assert_list)

    def assert_not(self, request, assert_list):
        return not all(self.process_assertion(request, assertion) for assertion in assert_list)

    def process_assertion(self, request, assertion):
        assertion_from = assertion.get(ASSERTION.FROM.value)
        assertion_key = assertion.get(ASSERTION.KEY.value)
        assertion_value = assertion.get(ASSERTION.VALUE.value)
        assertion_type = assertion.get(ASSERTION.TYPE.value)

        if assertion_from == ASSERTION.RESPONSEBODY.value:
            actual_value = self.find_key_in_dict(request, assertion_key)
            return self.perform_assertion(actual_value, assertion_value, assertion_type)
        else:
            logger.error(f"{ASSERTION.ASSERT_EXCEPTION}: {assertion_from}")
            return False

    @staticmethod
    def perform_assertion(actual_value, expected_value, assertion_type):
        actual_values = str(actual_value)
        try:
            if assertion_type == ASSERTION.EQUAL.value:
                if actual_values == expected_value:
                    assert_result = actual_values == expected_value
                    logger.info(f"{ASSERTION.RESPONSE.value}{actual_values}"
                                f"{ASSERTION.EQUAL.value}"
                                f"{ASSERTION.ASSERTION_VALUE.value}"
                                f"{expected_value}")
                    logger.info(f'{ASSERTION.ASSERTION_SUCCESS.value}')
                    logger.debug(assert_result)
                    return assert_result
                elif actual_values != expected_value:
                    logger.error(f"{ASSERTION.RESPONSE.value}"
                                 f"{actual_values}"
                                 f"{ASSERTION.NOTEQUALTO.value}"
                                 f"{ASSERTION.ASSERTION_VALUE.value}"
                                 f"{expected_value}")
                    logger.error(f'{ASSERTION.ASSERTION_FAILED.value}')
            elif assertion_type == ASSERTION.NOTEQUALTO.value:
                if actual_values != expected_value:
                    assert_result = actual_values != expected_value
                    logger.info(f"{ASSERTION.RESPONSE.value}"
                                f"{actual_values}"
                                f"{ASSERTION.NOTEQUALTO.value}"
                                f"{ASSERTION.ASSERTION_VALUE.value}"
                                f"{expected_value}")
                    logger.info(f'{ASSERTION.ASSERTION_SUCCESS.value}')
                    return assert_result
                elif actual_values == expected_value:
                    logger.error(
                        f"{ASSERTION.RESPONSE.value}"
                        f"{actual_values}"
                        f"{ASSERTION.EQUAL.value}"
                        f"{ASSERTION.ASSERTION_VALUE.value}"
                        f"{expected_value}")
                    logger.error(f'{ASSERTION.ASSERTION_FAILED.value}')
            else:
                logger.error(f"{ASSERTION.ASSERTION_FAILED.value}")
                return False
        except Exception as e:
            logger.error(f"{ASSERTION.ABNORMAL.value}{str(e)}")
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
