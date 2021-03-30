from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import WebMentionResponse


class WebMentionResponseAdmin(ModelAdmin):
    model = WebMentionResponse

    menu_label = "Webmention"
    menu_icon = "placeholder"

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

