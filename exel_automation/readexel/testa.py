
# class TestCase():
#     case_number = ""
#     case_name = ""
#     case_title = ""
#     api_url = ""
#     request_method = ""
#     main_api = ""
#     headers = ""
#     body = ""
#     execute = ""
#     assertion = ""
#     parameterize = ""
#     parameter_data = ""
#
#
# class ExcelFileReader:
#
#     def read_file(self, sheet_index=0, start_row=1):
#         workbook = xlrd.open_workbook(excelPath)
#         sheet = workbook.sheet_by_index(sheet_index)
#
#         test_cases = []
#
#         header = [
#             GloablEnum.CASE_NUMBER.value,
#             GloablEnum.CASE_NAME.value,
#             GloablEnum.CASE_TITLE.value,
#             GloablEnum.API_URL.value,
#             GloablEnum.REQUEST_METHOD.value,
#             GloablEnum.MAIN_API.value,
#             GloablEnum.HEADERS.value,
#             GloablEnum.BODY.value,
#             GloablEnum.EXECUTE.value,
#             GloablEnum.ASSERTION.value,
#             GloablEnum.PARAMETERIZE.value,
#             GloablEnum.PARAMETER_DATA.value
#         ]
#
#         for row_index in range(start_row, sheet.nrows):
#             row_data = sheet.row_values(row_index)
#             test_case = TestCase()
#             logger.debug(f'{row_index}{GloablEnum.EXEL_ROW_INDEX.value}{row_data}')
#             for index, attr_name in enumerate(header):
#                 setattr(test_case, attr_name, row_data[index])
#
#             test_cases.append(test_case)
#
#         return test_cases

