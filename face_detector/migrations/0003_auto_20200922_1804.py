# Generated by Django 3.1.1 on 2020-09-23 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('face_detector', '0002_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/known_faces/Sentdex')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_image', to='face_detector.user')),
            ],
        ),
    ]
