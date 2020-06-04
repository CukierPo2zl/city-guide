from django.urls import path
from .views import PlanAPIView, PlanListView


urlpatterns = [
    path('create', PlanAPIView.as_view()),
    path('', PlanListView.as_view()),
]