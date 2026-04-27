import random
from rest_framework import viewsets, permissions


from dlrApp.models import Client
from dlrApp.helper.pagination import StandardResultsSetPagination
from dlrApp.serializers.clientSerializer import ClientSerializer

from django.db.models import Q

from rest_framework.exceptions import ValidationError

from rest_framework.permissions import AllowAny


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        name = serializer.validated_data.get("name")
        smppUsername = serializer.validated_data.get("name")
        clean_name = name.replace(" ", "")
        safe_smpp_username = clean_name[:10]

        prefix = clean_name[:4]  # Gets up to 4 chars
        suffix_d = random.randint(1000, 9999)  # 4 digits
        suffix_f = random.randint(1000, 9999)  # 4 digits
        suffix_p = random.randint(1000, 9999)  # 4 digits

        finalDsmppUsername = f"{safe_smpp_username}{suffix_d}"
        finalFsmppUsername = f"{safe_smpp_username}{suffix_f}"
        safe_smpp_password = f"{prefix}{suffix_p}"
        print("nam1111111111111111111111111111111111111e", name)
        exist = Client.objects.filter(
            Q(name__iexact=name),
            isDeleted=False,
        )
        if exist.exists():
            raise ValidationError(
                {"error": "Client with this name or smppUsername already exists."}
            )

        clean_name = name.replace(" ", "")

        serializer.save(
            DsmppUsername=finalDsmppUsername,
            FsmppUsername=finalFsmppUsername,
            smppPassword=safe_smpp_password,
        )
