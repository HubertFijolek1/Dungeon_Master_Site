from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from campaigns.views import DMDashboardView, PlayerDashboardView

def home_view(request):
    return JsonResponse({"message": "Dungeon Master Website API"}, status=200)

def health_check(request):
    return JsonResponse({"status": "OK"}, status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('campaigns/', include(('campaigns.urls', 'campaigns'), namespace='campaigns')),
    path('characters/', include(('characters.urls', 'characters'), namespace='characters')),
    path('world/', include(('world.urls', 'world'), namespace='world')),
    path('mechanics/', include(('mechanics.urls', 'mechanics'), namespace='mechanics')),
    path('interactions/', include(('interactions.urls', 'interactions'), namespace='interactions')),
    path('health/', health_check, name='health_check'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dm/dashboard/', DMDashboardView.as_view(), name='dm_dashboard'),
    path('player/dashboard/', PlayerDashboardView.as_view(), name='player_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)