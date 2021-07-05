"""Base class for ciukune plugins app config."""
from typing import Iterable

from django.apps import AppConfig
from django.urls.resolvers import URLPattern

class CiukuneAppConfig(AppConfig):

    def get_urls(self) -> Iterable[URLPattern]:
        return []
