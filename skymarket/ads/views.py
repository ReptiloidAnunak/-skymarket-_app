import json

from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView,\
    UpdateAPIView, DestroyAPIView
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdsView(ListCreateAPIView):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AdDetailSerializer
        return AdSerializer

    def perform_create(self, serializer):
        if self.request.method == "POST":
            user = self.request.user
            try:
                serializer.save(author=user)
            except Exception:
                raise ValueError("Зарегистрируйтесь для размещения объявления")
            ad = Ad.objects.filter(id=user.pk).first()


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
#
# class Ad
