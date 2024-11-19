from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

def home_view(request):
    return JsonResponse({"message": "Dungeon Master Website API"}, status=200)

def health_check(request):
    return JsonResponse({"status": "OK"}, status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('campaigns.urls')),
    path('api/', include('campaigns.api_urls')),  # For API endpoints
    path('health/', health_check, name='health_check'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
