import uuid

import mongoengine as me
from django.contrib.auth.models import User
from django.db import models

from mainapp.models.test import Test, TextItem, TestDocument, BaseItem


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    version = models.IntegerField(default=1)
    max_grade = models.FloatField(default=0)

    show_correct = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    auto_checked = models.BooleanField(default=False)

    agree = models.BooleanField(default=False)

    pass_date = models.DateTimeField(auto_now_add=True)

class AnswerBaseItem(me.EmbeddedDocument):
    type = me.StringField(required=True, max_length=50)
    grade = me.FloatField(default=0,)
    meta = {"allow_inheritance": True}

class AnswerDocument(me.Document):
    id = me.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test_items = me.EmbeddedDocumentListField(BaseItem)
    items = me.ListField(me.EmbeddedDocumentField(AnswerBaseItem))

class AnswerChoiceItem(AnswerBaseItem):
    choices = me.ListField(me.IntField(min_value=0))

class AnswerTextItem(AnswerBaseItem):
    answer = me.StringField(max_length=5000, default="")
    similarity = me.FloatField(default=0)

