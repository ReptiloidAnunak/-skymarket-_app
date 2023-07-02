from django.urls import include, path
from rest_framework import routers

from ads import views



urlpatterns = [
    path("ads/", views.AdsView.as_view()),
    path("ads/<int:pk>/", views.AdDetailView.as_view()),
    path("ads/<int:ad_pk>/comments/", views.CommentsView.as_view()),
    path("ads/<int:ad_pk>/comments/<int:pk>/", views.CommentDetailView.as_view()),
]
