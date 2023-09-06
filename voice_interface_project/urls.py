# voice_interface_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # Import static function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('voice_interface_app.urls')),  # Include your app's URL configuration
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)