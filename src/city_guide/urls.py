from django.contrib import admin
from django.urls import path, include, re_path
from rest_auth.registration.views import VerifyEmailView, RegisterView
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import email_confirm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', email_confirm),
    path('api/users/', include('accounts.api.urls')),
    path('api/attraction/', include(('attraction.api.urls', 'attraction.api'),namespace='api-attraction')),
    path('api/plan/', include(('plan.api.urls', 'plan.api'),namespace='api-plan')),
    path('api/city/', include('city.api.urls')),
    path('api/category/', include('category.api.urls')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
