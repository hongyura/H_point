# Generated by Django 3.2.2 on 2021-05-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ranking',
            field=models.TextField(default='WELCOME'),
        ),
    ]
