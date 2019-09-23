from django.urls import path, include
from sdn_communication import views

urlpatterns = [
    path('desc_stats/', views.DescStatsView.as_view(), name='desc_api'),
    path('flow_stats/', views.FlowStatsView.as_view(), name='flow_api'),
    path('flow_agg_stats/', views.FlowAggregateStatsView.as_view(), name='flow_agg_api'),
    path('port_stats/', views.PortStatsView.as_view(), name='port_api'),
    path('flow_agg_diff/', views.FlowAggregateDiffStatsView.as_view(), name='flow_agg_diff_api'),
    path('port_diff/', views.PortDiffStatsView.as_view(), name='port_diff_api'),
    path('attack_notification/', views.AttackNotificationView.as_view(), name='attack_notification_api'),
    path('update_controller_IP/', views.UpdateControllerIPView.as_view(), name='update_controller_IP_api'),
]
