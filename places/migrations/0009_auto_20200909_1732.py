# Generated by Django 3.1 on 2020-09-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20200907_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
