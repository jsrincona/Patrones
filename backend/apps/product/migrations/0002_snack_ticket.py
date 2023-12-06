# Generated by Django 4.2.2 on 2023-07-01 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('n_stock', models.PositiveIntegerField(default=0)),
                ('t_type', models.CharField(max_length=255)),
            ],
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('d_creation', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('product.product',),
        ),
    ]
