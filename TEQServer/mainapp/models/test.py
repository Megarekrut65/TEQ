import uuid

from django.contrib.auth.models import User
from django.db import models

import mongoengine as me


class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

class TestMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class BaseItem(me.EmbeddedDocument):
    text = me.StringField(required=True, max_length=500)
    type = me.StringField(required=True, max_length=50)
    meta = {"allow_inheritance": True}

class TestDocument(me.Document):
    id = me.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = me.ListField(me.EmbeddedDocumentField(BaseItem))

class Choice(me.EmbeddedDocument):
    text = me.StringField(required=True, max_length=200)
    is_correct = me.BooleanField(default=False)

class ChoiceItem(BaseItem):
    choices = me.EmbeddedDocumentListField(Choice, required=True)

class TextItem(BaseItem):
    correct_answer = me.StringField(max_length=5000, default="")

