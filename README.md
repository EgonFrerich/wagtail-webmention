# wagtail-webmention 
[webmention](https://www.w3.org/TR/webmention/) for Django/Wagtail projects.

## What this project is

This package provides a way to integrate [webmention endpoint discovery](https://www.w3.org/TR/webmention/#sender-discovers-receiver-webmention-endpoint) and [webmention receipts](https://www.w3.org/TR/webmention/#receiving-webmentions) into your project. Once you follow the installation instructions, you should be able to use something like [webmention.rocks](https://webmention.rocks/) to generate a test webmention and see it in the Django admin panel.

Once you receive a webmention, you can click through to the page the webmention was sent from and see what people are saying about your site. Afterward, you can mark the webmention as reviewed in the Django admin so you can more easily see the latest webmentions you receive.

Once you verify that you're receiving webmentions successfully, you can use the webmention information as you like. As an example, you could query the webmentions that are responses to a specific page and display them on that page.

## Senden von webmention

Für das Senden wird auf Teile von https://github.com/beatonma/django-wm zurückgegriffen. 

Nicht enthalten ist das Senden einer webmention, wenn der Hinweis auf eine URL entfernt wird oder ein Beitrag mit einem Hinweis auf eine URL gelöscht wird.

Gesendet wird sofort mit der Veröffentlichung einer Seite; die Pufferung mit Celery ist von django-wm nicht übernommen.

## Installation

* Kopiere das Verzeichnis webmention in src wie eine Web-Anwendung in das betreffende Projekt
* Füge in settings ein
     *  'webmention' zu INSTALLED_APPS
     *  'wagtail.contrib.modeladmin' zu INSTALLED_APPS
     *  'webmention.middleware.webmention_middleware' zu MIDDLEWARE
     *  'APPEND_SLASH=False'
* Add the URL patterns to your top-level `urls.py`
    * `path('webmention/', include('webmention.urls'))`

Es ist eine logging-Funktion eingebaut (siehe outgoing_webmentions.py), die über den Ablauf informiert. Ggf. ist settings hierfür zu ergänzen, der Logger hat den Namen 'django'.

Zum Auffinden der Links in den auszuwertenden Texten wird das Paket beautifulsoup4 benötigt.

## Anwendung

Im Modell für die Page, für die webmention zu bearbeiten sind, ist zusätzlich MentionableMixin zu erben.

    from webmention.mixins import MentionableMixin
    ...
    class MeinePage(MentionableMixin, Page):

Dieses Modell muß die Funktion all_text implementieren, in der die auszuwertenden Inhalte der Seite bereitgestellt werden.

    def all_text(self) -> str:
            return f'{self.feld1} {self.feld2}'

Die Datenbank ist fortzuschreiben mit makemigrations und migrate.

## Hinweis
Z.Zt. sind view.py und resolution.py noch aus geforkten Repositories enthalten, sie werden aber anscheinend nicht benötigt. 




