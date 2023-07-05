
from rest_framework import pagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from ads.permissions import IsAdmin, IsOwner


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdsView(ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        return super(AdsView, self).get_permissions()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AdDetailSerializer
        return AdSerializer

    def perform_create(self, serializer):
        if self.request.method == "POST":
            user = self.request.user
            serializer.save(author=user)


class AdDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer

    def get_permissions(self):
        print(self.request.method)
        self.permission_classes = (IsAdmin, )
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated, ]
        elif self.request.method in ["UPDATE", "PATCH", "DELETE"]:
            self.permission_classes = (IsAdmin | IsOwner, )
            print(self.permission_classes)
        return super(AdDetailView, self).get_permissions()


class AdsMeView(ListAPIView):
    def get_queryset(self):
        author_pk = self.request.user.id
        queryset = self.model.objects.filter(author_id=author_pk)
        return queryset

    serializer_class = AdDetailSerializer
    model = serializer_class.Meta.model
    permission_classes = [IsAuthenticated]


class CommentsView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.kwargs.get("ad_pk"):
            ad_pk = self.kwargs.get("ad_pk")
            return self.queryset.filter(ad_id=ad_pk)
        else:
            raise Exception

    def perform_create(self, serializer):
        if self.request.method == "POST":
            user = self.request.user
            serializer.save(author=user)
            ad_pk = self.kwargs.get("ad_pk")
            serializer.save(ad_id=ad_pk)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        self.permission_classes = (IsAuthenticated,)
        if self.request.method == "GET":
            self.permission_classes = (IsAuthenticated,)
            print(self.permission_classes)
        elif self.request.method in ["GET", "UPDATE", "PATCH", "DELETE"]:
            self.permission_classes = (IsAdmin | IsOwner, )
            print(self.permission_classes)
        return tuple(permission() for permission in self.permission_classes)








