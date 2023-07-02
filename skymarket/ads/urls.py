from django.urls import include, path
from rest_framework import routers

from ads import views



urlpatterns = [
    path("ad/", views.AdsView.as_view()),
    path("ad/<int:pk>/", views.AdDetailView.as_view()),
    path("ad/<int:ad_pk>/comments/", views.CommentsView.as_view()),
    path("ad/<int:ad_pk>/comments/<int:pk>/", views.CommentsView.as_view())
]
