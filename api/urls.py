from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.views import ApplicationViewSet

router = DefaultRouter()

router.register('applications', ApplicationViewSet, basename='applications')

urlpatterns = [
    # path('v1/auth/', include(auth_urlpatterns)),
    path('v1/', include((router.urls, 'api'))),
]
