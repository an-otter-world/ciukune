# Copyright © 2019 STJV <contact@stjv.fr>
#
# This work is free. You can redistribute it and/or modify it under the terms
# of the Do What The Fuck You Want To Public License, Version 2, as published
# the comrade Sam Hocevar.
#
# See the COPYING file for more details.
""" Urls configuration """
from django.urls import include
from django.urls import path

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('v1/', include('api.urls')),
    path('saml/', include('saml.urls')),
]