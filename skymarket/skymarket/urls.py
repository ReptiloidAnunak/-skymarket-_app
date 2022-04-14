from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

# TODO здесь необходимо подклюючит нужные нам urls к проекту

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")



urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("", include(users_router.urls))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)