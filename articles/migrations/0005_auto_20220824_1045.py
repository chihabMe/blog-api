# Generated by Django 3.2.13 on 2022-08-24 10:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_published_alter_article_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 24, 10, 45, 38, 163925, tzinfo=utc)),
        ),
    ]
