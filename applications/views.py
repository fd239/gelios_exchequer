
from django.http import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from .models import Application
from .serializers import ApplicationSerializer

import requests

EXTERNAL_BASE_REQUEST_URL = 'http://172.31.17.100/c2_test3_gelios/hs/Exchequer_Services/Applications/'


class ApplicationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    @action(detail=False)
    def confirm(self, request):
        
        application_uuid = request.GET.get('application_uuid')
        data = {'user': 'web-user', 'password': 'pas001'}
        request_data = {'Application_UUID': application_uuid,
                        'Action': 'Confirmation'}
        
        response = requests.post(
            EXTERNAL_BASE_REQUEST_URL, 
            data=request_data, 
            auth=requests.auth.HTTPBasicAuth('web-user', 'pas001')
        )

        if response.status_code == 200:
            return HttpResponse(f'Заявка успешно согласована')
        elif response.status_code == 400:
            return HttpResponse(f'Заявка не согласована. Причина: {response.text}')
        else:
            return HttpResponse(f'Заявка не согласована')


    @action(detail=False)
    def decline(self, request):
        application_uuid = request.GET.get('application_uuid')
        return HttpResponse(f'заявка отклонена')
