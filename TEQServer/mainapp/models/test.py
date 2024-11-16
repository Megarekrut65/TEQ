import uuid

from django.db import models

from mainapp.models.user import UserProfile
import mongoengine as me


class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

class BaseItem(me.EmbeddedDocument):
    question_text = me.StringField(required=True, max_length=500)
    meta = {"allow_inheritance": True}

class TestItem(me.Document):
    id = me.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = me.ListField(me.EmbeddedDocumentField(BaseItem))

class Choice(me.EmbeddedDocument):
    text = me.StringField(required=True, max_length=200)
    is_correct = me.BooleanField(default=False)


class SingleAnswerItem(BaseItem):
    choices = me.EmbeddedDocumentListField(Choice, required=True)


class MultipleAnswerItem(BaseItem):
    choices = me.EmbeddedDocumentListField(Choice, required=True)


class TextAnswerItem(BaseItem):
    correct_answer = me.StringField(max_length=5000, default="")

