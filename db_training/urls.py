from django.urls import path
from .views import HelloView
from django.conf.urls import url

urlpatterns = [
    url(r'', HelloView.as_view(), name='index'),
]