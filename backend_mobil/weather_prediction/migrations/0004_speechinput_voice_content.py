# Generated by Django 4.1.3 on 2023-01-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weather_prediction", "0003_speechinput_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="speechinput",
            name="voice_content",
            field=models.TextField(null=True),
        ),
    ]
