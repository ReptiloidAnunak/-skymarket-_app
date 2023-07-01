import datetime

from django.conf import settings
from django.db import models
from users.models import User


class Ad(models.Model):
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at", "title")

    title = models.CharField(max_length=200, verbose_name="Название товара",
                             help_text="Введите название товара")

    price = models.PositiveIntegerField(default=0,
                                        verbose_name="Цена товара",
                                        help_text="Добавьте цену товара")

    description = models.CharField(max_length=1000,
                                   verbose_name="Описание товара",
                                   help_text="Введите описание товара")

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор", null=True)

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")

    image = models.ImageField(upload_to="images/",
                              verbose_name="Фото",
                              help_text="Разместите фото для объявления", null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ("-created_at",)

    text = models.CharField(max_length=3000,
                            verbose_name="Отзыв",
                            help_text="Оставьте свой отзыв о товаре")

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор", help_text="Автор отзыва")

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE,
                           verbose_name="Объявление")

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания",
                                      help_text="Дата написания объявления")

    def __str__(self):
        return f"{self.author}: {self.created_at} : {self.text}"