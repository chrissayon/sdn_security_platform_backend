from django.urls import path, include
from sdn_communication import views

urlpatterns = [
    path('desc_stats/', views.DescStatsView.as_view(), name='desc_api'),
    path('flow_stats/', views.FlowStatsView.as_view(), name='flow_api'),
    path('flow_agg_stats/', views.FlowAggregateStatsView.as_view(), name='flow_agg_api'),
    path('port_stats/', views.PortStatsView.as_view(), name='port_api'),
    path('flow_agg_diff/', views.PortStatsView.as_view(), name='flow_agg_diff_api'),
    path('port_diff/', views.PortDiffView.as_view(), name='port_diff_api'),
]
