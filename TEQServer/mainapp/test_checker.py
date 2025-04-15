from mainapp.item_types import SINGLE, MULTIPLE, TEXT
from mainapp.models.answer import Answer, AnswerDocument

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

def check_choice_item(answer_item, test_item):
    correct_answer, incorrect_answer = get_correct_count(answer_item, test_item)
    choices_correct = get_all_correct_count(test_item)

    grade_percent = (correct_answer - incorrect_answer)/choices_correct
    if grade_percent < 0:
        grade_percent = 0

    if not test_item.allow_proportion:
        grade_percent = int(grade_percent)

    answer_item.grade = test_item.grade * grade_percent

def check_text_item(answer_item, test_item):
    grade_percent = 0
    if answer_item.answer == test_item.correct_answer:
        grade_percent = 1

    answer_item.grade = test_item.grade * grade_percent

CHECK = {
    SINGLE: check_choice_item,
    MULTIPLE: check_choice_item,
    TEXT: check_text_item,
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