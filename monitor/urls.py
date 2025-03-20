from django.urls import path
from . import views
from .views import logout_view

from .views import anomaly_logs


urlpatterns = [
    path('log-analysis/', views.log_analysis, name='log_analysis'),

    path('logs/', anomaly_logs, name='anomaly_logs'),

    path('logout/', logout_view, name='logout'),

    path('', views.base, name='base'),
]
