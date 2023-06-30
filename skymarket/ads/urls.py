from django.urls import include, path

from ads import views


urlpatterns = [
    path("ad/", views.AdsView.as_view()),

    path("ad/<int:pk>/", views.AdDetailView.as_view()),

]
