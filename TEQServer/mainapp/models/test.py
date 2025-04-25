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
    can_share = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    auto_check = models.BooleanField(default=False)
    show_result = models.BooleanField(default=False)
    show_correct = models.BooleanField(default=False)

    version = models.IntegerField(default=1)

class TestMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class BaseItem(me.EmbeddedDocument):
    text = me.StringField(required=True, max_length=500)
    type = me.StringField(required=True, max_length=50)
    grade = me.FloatField(default=0,)
    allow_proportion = me.BooleanField(default=False)

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
    min_similar_percent = me.FloatField(default=0.0)
