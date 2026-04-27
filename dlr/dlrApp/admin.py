from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("name", "DsmppUsername", "FsmppUsername", "updatedAt", "isDeleted")

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
            {"fields": ("DsmppUsername", "FsmppUsername", "smppPassword")},
        ),
        (
            "Audit Metadata",
            {
                "fields": ("createdBy", "updatedBy", "createdAt", "updatedAt"),
                "description": "These fields are managed automatically.",
            },
        ),
    )

    # Make date fields read-only since they use auto_now
    readonly_fields = ("createdAt", "updatedAt")

    def save_model(self, request, obj, form, change):
        """
        Automatically set createdBy and updatedBy based on the logged-in user
        """
        if not change:  # If creating a new object
            obj.createdBy = request.user
        obj.updatedBy = request.user
        super().save_model(request, obj, form, change)
