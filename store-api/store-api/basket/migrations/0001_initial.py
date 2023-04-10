# Generated by Django 4.1.7 on 2023-03-09 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество товара')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clients', verbose_name='Клиент')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.products', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корине',
            },
        ),
    ]
