# Generated by Django 3.1.1 on 2020-09-23 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_detector', '0005_auto_20200922_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='face_detector/static/known_faces'),
        ),
    ]
