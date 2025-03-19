from django.urls import path
from . import views
from .views import logout_view

from .views import anomaly_logs


urlpatterns = [
    path('log-analysis/', views.log_analysis, name='log_analysis'),
    path('real-time-monitoring/', views.real_time_monitoring, name='real_time_monitoring'),

    path('logs/', anomaly_logs, name='anomaly_logs'),

    path('logout/', logout_view, name='logout'),

    path('', views.base, name='base'),
    path('logs/', views.anomaly_logs, name='anomaly_logs'),
]
