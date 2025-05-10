from celery import shared_task

from mainapp.models.answer import Answer
from mainapp.test_checker.checker import check_answer


@shared_task
def handle_auto_check_task(answer_id):
    """
    Task for answer checking
    :param answer_id:
    :return:
    """
    try:
        answer = Answer.objects.get(id=answer_id)
        check_answer(answer)
        print("handle_auto_check_task ended successfully")
    except Exception as e:
        print(e)
