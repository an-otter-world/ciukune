"""User views related class & utilities."""
from rest_framework.viewsets import ModelViewSet

from ciukune.core.models.user import User
from ciukune.core.serializers.user import UserSerializer

class UserViewSet(ModelViewSet):
    """User view set, providing standard user endpoints."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
