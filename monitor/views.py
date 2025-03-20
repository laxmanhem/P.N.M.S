from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from .models import AnomalyLog
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.shortcuts import render
from .models import Log  # Import your Log model


from django.http import JsonResponse
import json


def log_analysis(request):
    logs = AnomalyLog.objects.all().order_by('-timestamp')

    search_query = request.GET.get('search', '')
    protocol_filter = request.GET.get('protocol', '')
    anomaly_filter = request.GET.get('anomaly', '')

    if search_query:
        logs = logs.filter(Q(source_ip__icontains=search_query) | Q(destination_ip__icontains=search_query) | Q(anomaly_type__icontains=search_query))

    if protocol_filter:
        logs = logs.filter(protocol=protocol_filter)

    if anomaly_filter:
        logs = logs.filter(anomaly_type__icontains=anomaly_filter)

    return render(request, 'monitor/log_analysis.html', {'logs': logs})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def base(request):
    return render(request, 'monitor/base.html')

@login_required
def anomaly_logs(request):
    logs = AnomalyLog.objects.exclude(anomaly_type="Normal").order_by('-timestamp')

    search_query = request.GET.get('search', '')
    protocol_filter = request.GET.get('protocol', '')
    anomaly_filter = request.GET.get('anomaly', '')

    if search_query:
        logs = logs.filter(Q(source_ip__icontains=search_query) | Q(destination_ip__icontains=search_query))

    if protocol_filter:
        logs = logs.filter(protocol=protocol_filter)

    if anomaly_filter:
        logs = logs.filter(anomaly_type__icontains=anomaly_filter)

    logs = logs[:50]

    return render(request, 'monitor/logs.html', {'logs': logs})

