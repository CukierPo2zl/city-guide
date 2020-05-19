from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include, url
from .views import PlanRUDView, PlanAPIView
urlpatterns = [
    url(r'examples', PlanAPIView.as_view(), name='plan_create'),
    url(r'yourplans', PlanRUDView.as_view(), name='plan_rud')
]