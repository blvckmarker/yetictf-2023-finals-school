# Generated by Django 3.2.18 on 2023-04-14 09:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('secretkeys', '0005_alter_secretkeys_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretkeys',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 14, 9, 6, 53, 473797, tzinfo=utc)),
        ),
    ]
