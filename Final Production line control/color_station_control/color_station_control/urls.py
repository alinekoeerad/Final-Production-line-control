from django.contrib import admin
from django.urls import path, include
from color_station_control import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('color_APP.models')),
]

if not settings.DEBUG:
    pass
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
