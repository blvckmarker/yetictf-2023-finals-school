# Generated by Django 3.2.18 on 2023-04-13 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20230413_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='extra_info',
        ),
        migrations.RemoveField(
            model_name='products',
            name='is_premium',
        ),
        migrations.DeleteModel(
            name='ProductsReviews',
        ),
    ]
