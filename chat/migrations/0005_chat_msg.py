# Generated by Django 4.1.2 on 2022-10-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_rename_chat_url_chat_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='msg',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
