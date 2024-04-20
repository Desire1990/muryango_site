from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    # re_path("^.*$", views.index),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
