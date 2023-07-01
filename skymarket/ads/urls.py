from django.urls import include, path
from rest_framework import routers

from ads import views

router = routers.SimpleRouter()
router.register("ad/<int:pk>/comments", views.CommentsViewSet)

urlpatterns = [
    path("ad/", views.AdsView.as_view()),
    path("ad/<int:pk>/", views.AdDetailView.as_view()),
    # path("ad/<int:pk>/comments/", views.CommentsView.as_view())

] + router.urls
