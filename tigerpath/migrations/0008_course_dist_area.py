# Generated by Django 2.0.3 on 2018-04-25 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigerpath', '0007_userprofile_user_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='dist_area',
            field=models.TextField(default=''),
        ),
    ]
