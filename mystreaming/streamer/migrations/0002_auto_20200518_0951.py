# Generated by Django 3.0.6 on 2020-05-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='key',
            field=models.CharField(default='3d420cdecc839d9a60f1', max_length=20, unique=True),
        ),
    ]
