from django.conf import settings
from django.db import models


class Client(models.Model):
    id = models.IntegerField(primary_key=True, help_text="Manual ID entry")
    name = models.CharField(max_length=255)

    DsmppUsername = models.CharField(max_length=255)
    FsmppUsername = models.CharField(max_length=255)
    smppPassword = models.CharField(max_length=255)

    isDeleted = models.BooleanField(default=False)
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="puskarclient_created",
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="puskarclient_updated",
    )
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updatedAt"]
        db_table = "squadServices_puskar_client"  # Add this line

    def __str__(self):
        return self.name
