from mainapp.api.code_tester import run_code_tests
from mainapp.api.pl_similarity import calculate_similarity
from mainapp.models.answer import AnswerScriptUnitTestItem, AnswerUnitTestFailure, AnswerScriptItem
from mainapp.models.test import ScriptUnitTestItem, ScriptItem
from mainapp.test_checker.text import check_text_item


def convert_unittests(unittests_field):
    return [{"inTest":unittest.in_test, "outTest": unittest.out_test, "prefix":unittest.prefix} for unittest in unittests_field]

def check_unittests(unittests_field, language, function_structure, function_type, script):
    unittests = convert_unittests(unittests_field)

    data = run_code_tests(language, function_structure, function_type, unittests, script)
    failures = [AnswerUnitTestFailure(test_name=fail["testName"], reason=fail["reason"])
                for fail in data["failures"]]

    return data["passed"], failures, data["totalTests"]

def check_script_unittest_item(answer_item:AnswerScriptUnitTestItem, test_item: ScriptUnitTestItem):
    structure =test_item.function_structure
    type_ = test_item.function_type
    script = answer_item.answer

    try:
        data = check_unittests(test_item.public_unittests+test_item.private_unittests, test_item.language, structure, type_, script)
    except Exception as e:
        answer_item.grade = 0
        answer_item.error = str(e)
        return

    passed, failures, total = data

    answer_item.passed = passed
    answer_item.failures = failures
    answer_item.total_tests = total

    if answer_item.passed:
        answer_item.grade = test_item.grade
        return

    grade_percent = 0
    if test_item.allow_proportion:
        grade_percent = 1 - len(failures) / total

    answer_item.grade = round(test_item.grade * grade_percent, 2)

def check_script_item(answer_item: AnswerScriptItem, test_item:ScriptItem, similarity_api=calculate_similarity):
    return check_text_item(answer_item, test_item, similarity_api)