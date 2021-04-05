from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import WebMentionResponse, OutgoingWebmentionStatus


class WebMentionResponseAdmin(ModelAdmin):
    model = WebMentionResponse

    fields = [
        ("source_for_admin", "response_to_for_admin"),
        "response_body",
        ("date_created", "date_modified"),
        ("reviewed", "current"),
    ]

    readonly_fields = [
        "response_body",
        "source_for_admin",
        "response_to_for_admin",
        "date_created",
        "date_modified",
        "current",
    ]

    list_display = [
        "pk",
        "source_for_admin",
        "response_to_for_admin",
        "date_created",
        "date_modified",
        "reviewed",
        "current",
    ]

    list_editable = ["reviewed"]

    list_filter = ["reviewed", "current"]

    date_hierarchy = "date_modified"


modeladmin_register( WebMentionResponseAdmin)

class OutgoingWebmentionStatusAdmin(ModelAdmin):
    model = OutgoingWebmentionStatus
    readonly_fields = [
        'created_at',
        'source_url',
        'target_url',
        'target_webmention_endpoint',
        'status_message',
        'response_code',
        'successful',
    ]
    list_display = [
        'source_url',
        'target_url',
        'successful',
        'created_at',
    ]
    date_hierarchy = 'created_at'

modeladmin_register( OutgoingWebmentionStatusAdmin)

