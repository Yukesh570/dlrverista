from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        "id",
        "name",
        "DsmppUsername",
        "FsmppUsername",
        "updatedAt",
        "isDeleted",
    )

    # Clickable links
    list_display_links = ("name",)

    # Filters on the right sidebar
    list_filter = ("isDeleted", "createdAt", "updatedAt")

    # Search functionality
    search_fields = ("name", "DsmppUsername", "FsmppUsername")

    # Organization in the edit form
    fieldsets = (
        ("Client Information", {"fields": ("id", "name", "isDeleted")}),
        (
            "SMPP Credentials",
            {
                "fields": (
                    "DsmppUsername",
                    "FsmppUsername",
                    "smppPassword",
                    "is_limit",
                    "expireDate",
                )
            },
        ),
        (
            "Audit Metadata",
            {
                "fields": ("createdAt", "updatedAt"),
                "description": "These fields are managed automatically.",
            },
        ),
    )

    # Make date fields read-only since they use auto_now
    readonly_fields = ("id", "createdAt", "updatedAt")
