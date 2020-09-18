from django.urls import path
from .views import confirm, decline

urlpatterns = [
    path('confirm/', confirm, name='application confirm'),
    path('decline/', decline, name='application decline'),
]
