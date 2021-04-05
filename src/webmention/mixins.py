import logging
from django.dispatch import receiver
from wagtail.core.signals import page_published
from django.contrib.contenttypes.models import ContentType
from django.db import models

#from mentions.models.webmention import Webmention
from webmention.tasks import process_outgoing_webmentions
#from mentions.util import serialize_mentions

log = logging.getLogger(__name__)


class MentionableMixin(models.Model):
    class Meta:
        abstract = True

    def all_text(self) -> str:
        """
        Return all the text that should be searched when looking for
        outgoing Webmentions. Any URLs found in this text will be
        checked for webmention support.

        Typically this will just be the main text of your model but
        you may also want to include content from any other text fields
        such as a summary or abstract.

        Example:
            def all_text(self) -> str:
                return f'{self.introduction} {self.main_content}'
        """
        log.warning(
            'This model extends WebMentionableMixin but has not '
            'implemented all_text() so outgoing webmentions will '
            'not work!')
        return ''

    @receiver(page_published)
    def do_stuff_on_page_published(sender, **kwargs):
        page = kwargs['instance']
        log.info('Outgoing webmention processing task added to queue...')
        process_outgoing_webmentions(page.full_url, page.all_text())


