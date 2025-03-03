
from django.urls import path # type: ignore
from .views import viewReferral

urlpatterns = [
    path('', viewReferral, name='referrals'),
]
