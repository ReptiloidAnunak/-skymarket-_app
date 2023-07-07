# Generated by Django 3.2.6 on 2023-07-08 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ('-created_at', 'title'), 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(default=None, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.CharField(default=None, help_text='Введите описание товара', max_length=1000, verbose_name='Описание товара'),
        ),
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, default=None, help_text='Разместите фото для объявления', null=True, upload_to='ad_images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='Добавьте цену товара', verbose_name='Цена товара'),
        ),
        migrations.AddField(
            model_name='ad',
            name='title',
            field=models.CharField(default=None, help_text='Введите название товара', max_length=200, verbose_name='Название товара'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ads.ad', verbose_name='Объявление'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=None, help_text='Автор отзыва', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=None, help_text='Дата написания объявления', verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.CharField(default=None, help_text='Оставьте свой отзыв о товаре', max_length=3000, verbose_name='Отзыв'),
        ),
    ]