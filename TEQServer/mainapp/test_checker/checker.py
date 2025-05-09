from mainapp.item_types import SINGLE, MULTIPLE, SHORT, FULL, SCRIPT, SCRIPT_UNITTEST
from mainapp.models.answer import Answer, AnswerDocument
from mainapp.test_checker.choice import check_choice_item
from mainapp.test_checker.script import check_script_unittest_item, check_script_item
from mainapp.test_checker.text import check_text_item

CHECK = {
    SINGLE: check_choice_item,
    MULTIPLE: check_choice_item,
    SHORT: check_text_item,
    FULL: check_text_item,
    SCRIPT: check_script_item,
    SCRIPT_UNITTEST: check_script_unittest_item
}

def check_answer(answer:Answer):
    doc = AnswerDocument.objects.get(pk=answer.pk)
    test_items = doc.test_items
    items = doc.items

    for i in range(len(test_items)):
        test_item = test_items[i]
        answer_item = items[i]

        try:
            CHECK[test_item.type](answer_item, test_item)
        except Exception as e:
            print(e)

    answer.checked = answer.test.show_result
    answer.auto_checked = True
    answer.save()
    doc.save()