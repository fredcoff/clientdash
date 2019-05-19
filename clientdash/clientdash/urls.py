from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('api/clients', include('clients.urls')),
    url('api/auth', include('accounts.urls')),
    url('', include('frontend.urls'))
]
