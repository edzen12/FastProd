from rest_framework import viewsets, mixins

from .serializers import SocialSerializer
from .models import Social


class SocialViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer