from mainapp.models.answer import AnswerChoiceItem
from mainapp.models.test import ChoiceItem

def get_choices_summary(answer_item:AnswerChoiceItem, test_item:ChoiceItem):
    """
    Returns count of correct and incorrect answers
    :param answer_item:
    :param test_item:
    :return:
    """
    correct_answer = 0
    incorrect_answer = 0

    for choice_index in answer_item.choices:
        if test_item.choices[choice_index].is_correct:
            correct_answer += 1
        else:
            incorrect_answer += 1

    return correct_answer, incorrect_answer

def get_correct_count(test_item:ChoiceItem):
    """
    Returns count of correct answers
    :param test_item:
    :return:
    """
    choices_correct = 0

    for choice in test_item.choices:
        if choice.is_correct:
            choices_correct += 1

    return choices_correct

def check_choice_item(answer_item:AnswerChoiceItem, test_item:ChoiceItem):
    correct_answer, incorrect_answer = get_choices_summary(answer_item, test_item)
    choices_correct = get_correct_count(test_item)

    grade_percent = (correct_answer - incorrect_answer)/choices_correct
    if grade_percent < 0:
        grade_percent = 0

    if not test_item.allow_proportion:
        grade_percent = int(grade_percent)

    answer_item.grade = test_item.grade * grade_percent