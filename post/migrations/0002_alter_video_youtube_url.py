# Generated by Django 5.1.6 on 2025-03-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='youtube_url',
            field=models.URLField(max_length=500),
        ),
    ]
