import uuid

from django.contrib.auth.models import User
from django.db import models

import mongoengine as me

from mainapp.models.test import Test, ChoiceItem, TextItem


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    pass_date = models.DateTimeField(auto_now_add=True)

class AnswerBaseItem(me.EmbeddedDocument):
    type = me.StringField(required=True, max_length=50)
    meta = {"allow_inheritance": True}

class AnswerDocument(me.Document):
    id = me.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    answers = me.ListField(me.EmbeddedDocumentField(AnswerBaseItem))

class AnswerChoiceItem(AnswerBaseItem):
    item = me.EmbeddedDocumentField(ChoiceItem)
    choices = me.ListField(me.IntField(min_value=0))

class AnswerTextItem(AnswerBaseItem):
    item = me.EmbeddedDocumentField(TextItem)
    answer = me.StringField(max_length=5000, default="")

