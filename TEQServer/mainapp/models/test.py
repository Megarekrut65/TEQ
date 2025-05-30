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
    category = models.CharField(blank=True, null=True, max_length=100)

    can_share = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    auto_check = models.BooleanField(default=False)
    show_result = models.BooleanField(default=False)
    show_correct = models.BooleanField(default=False)

    answer_count = models.IntegerField(default=0)

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

class ScriptItem(TextItem):
    language = me.StringField(required=True, max_length=50)

class UnitTest(me.EmbeddedDocument):
    in_test = me.StringField(required=True, max_length=500)
    out_test = me.StringField(required=True, max_length=200)
    prefix = me.StringField(required=False, default="", max_length=50)

class ScriptUnitTestItem(ScriptItem):
    function_structure = me.StringField(default="", max_length=500)
    function_type = me.StringField(required=True, max_length=50) # integer, float, string, bool
    public_unittests = me.EmbeddedDocumentListField(UnitTest, required=True)
    private_unittests = me.EmbeddedDocumentListField(UnitTest, required=True)
