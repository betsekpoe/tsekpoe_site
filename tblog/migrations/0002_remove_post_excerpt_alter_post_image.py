# Generated by Django 5.1.4 on 2025-03-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='tblog/images/'),
        ),
    ]
