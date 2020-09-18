
from rest_framework import viewsets, mixins

from applications.models import Application
from applications.serializers import ApplicationSerializer

EXTERNAL_BASE_REQUEST_URL = 'http://172.31.17.100/c2_test3_gelios/hs/Exchequer_Services/Applications/'


class ApplicationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()