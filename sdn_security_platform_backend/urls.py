from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from sdn_communication import views

urlpatterns = [
    path('graphAPI/', include('graphAPI.urls')),
    path('admin/', admin.site.urls),
    path('sdn_communication/', include('sdn_communication.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)