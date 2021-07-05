"""Tovarich core app."""
from typing import Iterable
from os.path import dirname

from django.urls.resolvers import URLPattern

from ciukune.core.utils.apps import CiukuneAppConfig

_LIST_VIEW_MAPPING = {
    'get': 'list',
}

_OBJECT_VIEW_MAPPING = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

class AppConfig(CiukuneAppConfig):
    """AppConfig implementation for ciukune core."""
    name = 'ciukune.core'
    label = 'ciukune'
    path = dirname(__file__)

    def get_urls(self) -> Iterable[URLPattern]:
        from django.urls import include
        from django.urls import path
        from django.urls import re_path
        from django.views.generic import TemplateView
        from rest_framework_simplejwt.views import TokenObtainPairView
        from rest_framework_simplejwt.views import TokenRefreshView

        from ciukune.core.views.user.me import MeView
        from ciukune.core.views.user import UserViewSet

        yield re_path(r'api/',
            include([
                path('auth/login', TokenObtainPairView.as_view(), name='login'),
                path('auth/refresh', TokenRefreshView.as_view(), name='refresh'),
                path('user/me', MeView.as_view(), name='me'),
                path('user', UserViewSet.as_view(_LIST_VIEW_MAPPING), name='user'),
                path('user/<int:pk>', UserViewSet.as_view(_OBJECT_VIEW_MAPPING), name='user_detail'),
            ])
        )
        yield re_path(r'^(?!api).*$', TemplateView.as_view(template_name="index.html"), name="index")
