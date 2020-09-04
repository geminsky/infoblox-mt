import uuid
from django.db import models


class Data(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    enabled = models.BooleanField(default=False)


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    data = models.ManyToManyField(Data)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
