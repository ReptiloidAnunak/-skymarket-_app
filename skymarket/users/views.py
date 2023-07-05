from users.serializers import CurrentUserSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from users.models import User
from rest_framework.permissions import IsAuthenticated


class CurrentUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer
    permission_classes = [IsAuthenticated]

