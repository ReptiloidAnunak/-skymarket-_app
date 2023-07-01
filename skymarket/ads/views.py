import json

from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


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


class AdDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        ad_obj = get_object_or_404(Ad, id=ad_id)
        return ad_obj.comments.all()


