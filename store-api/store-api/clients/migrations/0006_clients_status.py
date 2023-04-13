# Generated by Django 4.0 on 2023-04-09 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_remove_clients_login_clients_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='status',
            field=models.CharField(choices=[('default', 'DEFAULT'), ('premium', 'PREMIUM')], default='default', max_length=255, verbose_name='Статус'),
            preserve_default=False,
        ),
    ]