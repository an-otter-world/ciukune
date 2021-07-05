"""Urls for ciukune core."""
from django.apps import apps
from ciukune.core.utils.apps import CiukuneAppConfig

urlpatterns = []

for config in apps.get_app_configs():
    if not isinstance(config, CiukuneAppConfig):
        continue
    urlpatterns = urlpatterns + list(config.get_urls())

