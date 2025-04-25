import uuid

from django.contrib.auth.models import User
from django.db import models

import mongoengine as me

from mainapp.models.test import BaseItem


class TestPool(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class TestCategory(me.Document):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pool_id = me.UUIDField()
    name = me.StringField(max_length=100)
    items = me.ListField(me.EmbeddedDocumentField(BaseItem))