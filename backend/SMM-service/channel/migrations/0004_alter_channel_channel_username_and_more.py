# Generated by Django 5.0.3 on 2024-04-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channel", "0003_channel_channel_username_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="channel_username",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="channelrequest",
            name="channel_username",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
