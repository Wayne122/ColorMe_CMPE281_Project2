# Generated by Django 2.2.6 on 2019-11-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s3objects', '0007_auto_20191012_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='s3objects',
            name='new_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
