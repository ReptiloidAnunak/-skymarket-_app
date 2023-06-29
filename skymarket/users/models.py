from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choices = ((USER, USER),
               (ADMIN, ADMIN),
              )


class User(AbstractBaseUser):

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите имя, макс 50 символов",null=True
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите фамилию, макс 50 символов",null=True
    )

    email = models.EmailField(
        "email address",
        unique=True,
        help_text="Укажите контактный имейл",null=True
    )

    phone = PhoneNumberField(
        verbose_name="Телефон для связи",
        help_text="Введите номер контактного телефона", null=True

    )

    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="Роль пользователя",
        help_text="Выберите роль пользователя",
    )

    is_active = models.BooleanField(
        verbose_name="Аккаунт активен",null=True
    )

    image = models.ImageField(null=True)

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

