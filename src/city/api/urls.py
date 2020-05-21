from django.urls import path
from .views import CitiesView
urlpatterns = [
    path('', CitiesView.as_view())
]