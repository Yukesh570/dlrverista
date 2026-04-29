from django.conf import settings
from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    DsmppUsername = models.CharField(max_length=255)
    FsmppUsername = models.CharField(max_length=255)
    smppPassword = models.CharField(max_length=255)
    expireDate = models.DateField(null=True, blank=True)
    isDeleted = models.BooleanField(default=False)

    createdAt = models.DateTimeField(auto_now_add=True)

    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updatedAt"]
        db_table = "squadServices_puskar_client"  # Add this line

    def __str__(self):
        return self.name
