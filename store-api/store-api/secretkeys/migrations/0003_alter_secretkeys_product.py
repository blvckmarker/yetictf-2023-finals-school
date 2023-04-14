# Generated by Django 3.2.18 on 2023-04-14 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20230413_1747'),
        ('secretkeys', '0002_alter_secretkeys_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretkeys',
            name='product',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='products.products', verbose_name='Product'),
        ),
    ]