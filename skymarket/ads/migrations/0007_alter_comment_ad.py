# Generated by Django 3.2.6 on 2023-07-01 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ad', verbose_name='Объявление'),
        ),
    ]