# Generated by Django 3.2.7 on 2021-12-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20211223_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='customer',
            name='picture',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]
