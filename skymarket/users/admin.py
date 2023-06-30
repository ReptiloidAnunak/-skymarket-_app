from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User
from ads.models import Ad, Comment
admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Comment)