from django.contrib import admin
from django.urls import path,include
from django.conf import settings  # < here
from django.conf.urls.static import static

import main.views
from main.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/flight/', include('flight.urls')),
    path('booking/', include('flight.urls')),
    path('', include('cvbuilder.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

