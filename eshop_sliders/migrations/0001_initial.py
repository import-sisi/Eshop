# Generated by Django 3.2 on 2021-05-15 05:33

from django.db import migrations, models
import eshop_sliders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('link', models.URLField(max_length=100, verbose_name='آدرس')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_sliders.models.upload_image_path, verbose_name='تصویر')),
            ],
        ),
    ]
