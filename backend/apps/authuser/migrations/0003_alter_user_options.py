# Generated by Django 4.2.2 on 2023-07-01 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0002_customer_employee_user_n_id_user_n_phone_user_t_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuarios', 'verbose_name_plural': 'Usuario'},
        ),
    ]