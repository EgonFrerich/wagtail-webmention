# wagtail-webmention 
[webmention](https://www.w3.org/TR/webmention/) for Django/Wagtail projects.

## What this project is

This package provides a way to integrate [webmention endpoint discovery](https://www.w3.org/TR/webmention/#sender-discovers-receiver-webmention-endpoint) and [webmention receipts](https://www.w3.org/TR/webmention/#receiving-webmentions) into your project. Once you follow the installation instructions, you should be able to use something like [webmention.rocks](https://webmention.rocks/) to generate a test webmention and see it in the Django admin panel.

Once you receive a webmention, you can click through to the page the webmention was sent from and see what people are saying about your site. Afterward, you can mark the webmention as reviewed in the Django admin so you can more easily see the latest webmentions you receive.

Once you verify that you're receiving webmentions successfully, you can use the webmention information as you like. As an example, you could query the webmentions that are responses to a specific page and display them on that page.

## Senden von webmention

Das Senden ist  ebenfalls vorgesehen. Muß aber speziell eingerichtet werden.

## Installation

* Kopiere das Verzeichnis webmention in src wie eine Web-Anwendung in das betreffende Projekt
* Füge in settings ein
     *  'webmention' zu INSTALLED_APPS
     *  'wagtail.contrib.modeladmin' zu INSTALLED_APPS
     *  'webmention.middleware.webmention_middleware' zu MIDDLEWARE
* Add the URL patterns to your top-level `urls.py`
    * `path('webmention/', include('webmention.urls'))`




