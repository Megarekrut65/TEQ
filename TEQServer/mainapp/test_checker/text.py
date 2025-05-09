from mainapp.api.similarity import calculate_similarity
from mainapp.models.answer import AnswerTextItem
from mainapp.models.test import TextItem


def check_text_item(answer_item: AnswerTextItem, test_item:TextItem, similarity_api=calculate_similarity):
    grade_percent = 0
    if answer_item.answer == test_item.correct_answer:
        grade_percent = 1

    if answer_item.answer == "" or test_item.correct_answer == "":
        answer_item.grade = 0
        return

    try:
        similarity = similarity_api(answer_item.answer, test_item.correct_answer)

        if similarity * 100 >= test_item.min_similar_percent:
            grade_percent = 1
        answer_item.grade = round(test_item.grade * grade_percent, 2)

        answer_item.similarity = round(similarity*100, 2)
    except:
        answer_item.grade = 0
        answer_item.similarity = 0