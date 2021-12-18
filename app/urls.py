from django.urls import path
from .import views

urlpatterns = [
    path('',views.main1,name='main1')
]
