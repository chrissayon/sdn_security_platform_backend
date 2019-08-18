from django.urls import path, include
from sdn_communication import views

urlpatterns = [
    path('desc_stats/', views.DescStatsView.as_view(), name='desc-api'),
]
