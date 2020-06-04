from django.urls import path
from django.conf.urls import url
from .views import PlanAPIView, PlanListView, plan_delete


urlpatterns = [
    path('create', PlanAPIView.as_view()),
    path('', PlanListView.as_view()),
    url(r'^(?P<pk>[0-9]+)$', plan_delete),
]