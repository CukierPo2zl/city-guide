from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from .views import AttractionRUDView, AttractionAPIView, TrendingAttractions
urlpatterns = [
  url(r'^$', AttractionAPIView.as_view(), name='att_create'),
  url(r'^(?P<pk>\d+)/$', AttractionRUDView.as_view(), name='att_rud'),
  path('trending', TrendingAttractions.as_view())
]