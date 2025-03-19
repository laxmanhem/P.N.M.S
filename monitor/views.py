from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import AnomalyLog
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.shortcuts import render
from .models import Log  # Import your Log model


from django.http import JsonResponse
import json


def log_analysis(request):
    # Example log data (replace with real log fetching/analysis logic)
    logs = [
        {"timestamp": "2025-03-18 12:30:00", "message": "Anomaly detected in network traffic", "level": "ERROR"},
        {"timestamp": "2025-03-18 12:45:00", "message": "Network traffic normal", "level": "INFO"},
        # Add more log entries as needed
    ]

    # You can add log analysis logic here if needed

    # If the request is AJAX (for fetching logs dynamically)
    if request.is_ajax():
        return JsonResponse({'logs': logs})

    # Otherwise, render the log analysis page (for regular navigation)
    return render(request, 'log_analysis.html', {'logs': logs})


def real_time_monitoring(request):
    return render(request, 'network_monitor/real_time_monitoring.html')



def anomaly_logs(request):
    logs = Log.objects.all()

    search_query = request.GET.get('search', '')
    protocol_filter = request.GET.get('protocol', '')
    anomaly_filter = request.GET.get('anomaly', '')

    # Filtering logic
    if search_query:
        logs = logs.filter(source_ip__icontains=search_query) | logs.filter(destination_ip__icontains=search_query)

    print(protocol_filter)

    if protocol_filter:
        logs = logs.filter(protocol=protocol_filter)

    if anomaly_filter:
        logs = logs.filter(anomaly_type=anomaly_filter)

    return render(request, 'logs.html', {'logs': logs})





def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def base(request):
    return render(request, 'monitor/base.html')

@login_required
def anomaly_logs(request):
    logs = AnomalyLog.objects.all().order_by('-timestamp')[:50]
    return render(request, 'monitor/logs.html', {'logs': logs})

