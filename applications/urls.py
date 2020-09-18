from django.urls import path
from .views import confirm, decline

urlpatterns = [
    # path('v1/auth/', include(auth_urlpatterns)),
    path('confirm/', confirm, name='application confirm'),
    path('decline/', decline, name='application decline'),
]
