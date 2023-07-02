from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from users.models import UserRoles
from ads.models import Ad, Comment


class AdDetailPermission(BasePermission):
    message = 'Updating or deleting other users ads not allowed'

    def has_permission(self, request, view):
        ad = get_object_or_404(Ad, pk=view.kwargs["pk"])

        if request.method == "GET":
            if not bool(request.user and request.user.is_authenticated):
                raise AttributeError("You should login to see any ad in details")
            return True

        elif request.method in ["PATCH", "PUT", "UPDATE", "DELETE"]:
            try:
                user_role = request.user.role
            except AttributeError:
                raise AttributeError("You should login to see any ad and its comments")
            if request.user.role == UserRoles.ADMIN:
                return True
            elif ad.author_id == request.user.id:
                return True
            return False


class CommentDetailPermission(BasePermission):
    message = 'Updating or deleting other users ads not allowed'

    def has_permission(self, request, view):
        comment = get_object_or_404(Comment, pk=view.kwargs["pk"])

        if request.method == "GET":
            if not bool(request.user and request.user.is_authenticated):
                raise ValueError("You should login to see any comment")
            return True

        elif request.method in ["PATCH", "PUT", "UPDATE", "DELETE"]:
            try:
                user_role = request.user.role
            except AttributeError:
                raise AttributeError("You should login to see any ad and its comments")

            if request.user.role == UserRoles.ADMIN:
                return True
            elif comment.author_id == request.user.id:
                return True
            return False

