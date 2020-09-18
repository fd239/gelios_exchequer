
from django.http import HttpResponse
import requests

EXTERNAL_BASE_REQUEST_URL = 'http://172.31.17.100/c2_test3_gelios/hs/Exchequer_Services/Applications/'


def confirm(request):

    application_uuid = request.GET.get('application_uuid')

    if application_uuid is None:
        return HttpResponse('Переданы не верные параметры')

    request_data = {'Application_UUID': application_uuid,
                    'Action': 'Confirm'}

    external_response = send_external_request(request_data)

    if external_response.status_code == 200:
        response_dict = external_response.json()
        return HttpResponse(response_dict['Comment'])
    elif external_response.status_code == 400:
        return HttpResponse('Заявка не согласована')
    else:
        return HttpResponse('Заявка не согласована')


def decline(request):
    application_uuid = request.GET.get('application_uuid')

    request_data = {'Application_UUID': application_uuid,
                    'Action': 'Decline'}

    external_response = send_external_request(request_data)

    if external_response.status_code == 200:
        return HttpResponse('заявка отклонена')
    else:
        return HttpResponse('Заявка не отклонена')


def send_external_request(request_data):
    response = requests.post(
        EXTERNAL_BASE_REQUEST_URL,
        json=request_data,
        auth=requests.auth.HTTPBasicAuth('web-user', 'pas001')
    )

    return response
