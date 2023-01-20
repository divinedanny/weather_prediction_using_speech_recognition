# Generated by Django 4.1.3 on 2023-01-11 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("weather_prediction", "0002_speechinput"),
    ]

    operations = [
        migrations.AddField(
            model_name="speechinput",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]