from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import admin
from django.urls import include, path
from rest_framework import routers

from ads.views import AdViewSet

ad_router = routers.SimpleRouter()
ad_router.register("ads", AdViewSet, basename="ads")


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("", include("ads.urls")),
    path("api/", include("users.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
