from django.conf import settings
from django.shortcuts import render

import requests
from .forms import DeclineReasonForm


def confirm(request):
    confirmation_code = request.GET.get('code')

    if confirmation_code is None:
        context = {'result': False, 'comment': 'Переданы неверные параметры'}
        return render(request, 'confirmation.html', context)

    request_data = {'confirmation_code': confirmation_code,
                    'action': 'confirm'}

    external_response = send_external_request(request_data)

    if external_response.status_code == 200:
        context = external_response.json()
    else:
        context = {'result': False, 'comment': 'Заявка не согласована. ' +
                   '\n' + external_response.text}

    return render(request, 'confirmation.html', context)


def decline(request):

    if request.method == 'POST':
        form = DeclineReasonForm(request.POST)

        if form.is_valid():
            confirmation_code = request.GET.get('code')

            if confirmation_code is None:
                context = {'result': False,
                           'comment': 'Переданы неверные параметры'
                           }

                return render(request, 'confirmation.html', context)

            request_data = {'confirmation_code': confirmation_code,
                            'action': 'decline',
                            'decline_reason': form.cleaned_data['decline_reason']
                            }

            external_response = send_external_request(request_data)

            if external_response.status_code == 200:
                context = external_response.json()
            else:
                context = {'result': False, 'comment': 'Заявка не отклонена. ' +
                           '\n' + external_response.text}

            return render(request, 'confirmation.html', context)
    else:
        form = DeclineReasonForm()
        return render(
            request,
            'decline.html',
            {'form': form, 'code': request.GET.get('code')}
        )


def send_external_request(request_data):
    return requests.post(
        settings.EXTERNAL_BASE_REQUEST_URL,
        json=request_data,
        auth=requests.auth.HTTPBasicAuth(
            settings.EXTERNAL_BASE_USER, settings.EXTERNAL_BASE_PASS)
    )
