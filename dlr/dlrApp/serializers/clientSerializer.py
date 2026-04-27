from rest_framework import serializers

from dlrApp.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "DsmppUsername",
            "FsmppUsername",
            "smppPassword",
            "createdAt",
        ]
        read_only_fields = [
            "id",
            "DsmppUsername",
            "FsmppUsername",
            "smppPassword",
        ]
