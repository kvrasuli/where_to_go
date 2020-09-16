# Generated by Django 3.1 on 2020-09-16 18:38

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20200909_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция в списке'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]