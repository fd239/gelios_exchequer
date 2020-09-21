from applications.models import Application
from applications.serializers import ApplicationSerializer

from rest_framework import viewsets, mixins


class ApplicationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
