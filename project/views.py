"""
The 3 endpoints for this practice target.

Function-based views keep things simple and easy to read.
"""
from django.http import HttpResponse, JsonResponse


def home(request):
    """GET / -> a short welcome that names the stack."""
    return HttpResponse("Welcome! This is a Python + Django practice app.")


def health(request):
    """GET /health -> a tiny JSON health check for probes / load balancers."""
    return JsonResponse({"status": "ok"}, status=200)


def items(request):
    """GET /api/items -> a small list so you can verify the app really works."""
    sample_items = [
        {"id": 1, "name": "Keyboard"},
        {"id": 2, "name": "Mouse"},
        {"id": 3, "name": "Monitor"},
        {"id": 4, "name": "Webcam"},
    ]
    return JsonResponse({"items": sample_items})
