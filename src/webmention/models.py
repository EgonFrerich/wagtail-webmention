from django.db import models
from django.utils.html import format_html


class WebMentionResponse(models.Model):
    response_body = models.TextField()
    response_to = models.URLField()
    source = models.URLField()
    reviewed = models.BooleanField(default=False)
    current = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "webmention"
        verbose_name_plural = "webmentions"

    def __str__(self):
        return self.source

    def source_for_admin(self):
        return format_html('<a href="{href}">{href}</a>'.format(href=self.source))

    source_for_admin.short_description = "source"

    def response_to_for_admin(self):
        return format_html('<a href="{href}">{href}</a>'.format(href=self.response_to))

    response_to_for_admin.short_description = "response to"

    def invalidate(self):
        if self.id:
            self.current = False
            self.save()

    def update(self, source, target, response_body):
        self.response_body = response_body
        self.source = source
        self.response_to = target
        self.current = True
        self.save()

class OutgoingWebmentionStatus(models.Model):
    """Status tracker for webmentions that you (attempt to) send from your server.

    Currently used primarily for logging of outgoing mentions.
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    source_url = models.URLField(
        help_text='The URL on your server where this mention originates',
    )
    target_url = models.URLField(
        help_text='The URL that you mentioned.',
    )
    target_webmention_endpoint = models.URLField(
        null=True,
        blank=True,
        help_text='The endpoint URL to which we sent the webmention',
    )
    status_message = models.CharField(
        max_length=1024,
        help_text='Success, or an explanation of what went wrong.',
    )
    response_code = models.PositiveIntegerField(default=0)

    successful = models.BooleanField(default=False)

    def __str__(self):
        return (f'{self.source_url} -> {self.target_url} '
                f'(endpoint={self.target_webmention_endpoint}): '
                f'[{self.successful}] {self.status_message} '
                f'[{self.response_code}]')

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Outgoing Webmention Statuses'

