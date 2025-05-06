from mainapp.api.python_tester import python_run_tests
from mainapp.api.similarity import calculate_similarity
from mainapp.item_types import SINGLE, MULTIPLE, SHORT, FULL, SCRIPT, SCRIPT_UNITTEST
from mainapp.models.answer import Answer, AnswerDocument, AnswerScriptUnitTestItem, AnswerTextItem, AnswerChoiceItem, \
    AnswerUnitTestFailure
from mainapp.models.test import ScriptUnitTestItem, TextItem, ChoiceItem


def get_correct_count(answer_item, test_item):
    correct_answer = 0
    incorrect_answer = 0

    for choice_index in answer_item.choices:
        if test_item.choices[choice_index].is_correct:
            correct_answer += 1
        else:
            incorrect_answer += 1

    return correct_answer, incorrect_answer

def get_all_correct_count(test_item):
    choices_correct = 0

    for choice in test_item.choices:
        if choice.is_correct:
            choices_correct += 1

    return choices_correct

def check_choice_item(answer_item:AnswerChoiceItem, test_item:ChoiceItem):
    correct_answer, incorrect_answer = get_correct_count(answer_item, test_item)
    choices_correct = get_all_correct_count(test_item)

    grade_percent = (correct_answer - incorrect_answer)/choices_correct
    if grade_percent < 0:
        grade_percent = 0

    if not test_item.allow_proportion:
        grade_percent = int(grade_percent)

    answer_item.grade = test_item.grade * grade_percent

def check_text_item(answer_item: AnswerTextItem, test_item:TextItem):
    grade_percent = 0
    if answer_item.answer == test_item.correct_answer:
        grade_percent = 1

    if answer_item.answer == "" or test_item.correct_answer == "":
        answer_item.grade = 0
        return

    try:
        similarity = calculate_similarity(answer_item.answer, test_item.correct_answer)

        if similarity * 100 >= test_item.min_similar_percent:
            grade_percent = 1
        answer_item.grade = round(test_item.grade * grade_percent, 2)

        answer_item.similarity = round(similarity*100, 2)
    except:
        answer_item.grade = 0
        answer_item.similarity = 0

def convert_unittests(unittests_field):
    return [{"inTest":unittest.in_test, "outTest": unittest.out_test, "prefix":unittest.prefix} for unittest in unittests_field]

def check_unittests(unittests_field, test_runner, function_structure, function_type, script):
    unittests = convert_unittests(unittests_field)

    data = test_runner(function_structure, function_type, unittests, script)
    failures = [AnswerUnitTestFailure(test_name=fail["testName"], reason=fail["reason"])
                for fail in data["failures"]]

    return data["passed"], failures, data["totalTests"]

def check_script_unittest_item(answer_item:AnswerScriptUnitTestItem, test_item: ScriptUnitTestItem):
    test_runner = python_run_tests

    structure =test_item.function_structure
    type_ = test_item.function_type
    script = answer_item.answer

    try:
        data = check_unittests(test_item.public_unittests+test_item.private_unittests, test_runner, structure, type_, script)
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


CHECK = {
    SINGLE: check_choice_item,
    MULTIPLE: check_choice_item,
    SHORT: check_text_item,
    FULL: check_text_item,
    SCRIPT: check_text_item,
    SCRIPT_UNITTEST: check_script_unittest_item
}

def check_test(answer:Answer):
    doc = AnswerDocument.objects.get(pk=answer.pk)
    test_items = doc.test_items
    items = doc.items

    for i in range(len(test_items)):
        test_item = test_items[i]
        answer_item = items[i]

        CHECK[test_item.type](answer_item, test_item)

    answer.checked = answer.test.show_result
    answer.auto_checked = True
    answer.save()
    doc.save()