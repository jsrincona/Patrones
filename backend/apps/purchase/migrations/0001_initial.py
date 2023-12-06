# Generated by Django 4.2.2 on 2023-07-01 23:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('pk_id', models.AutoField(primary_key=True, serialize=False)),
                ('n_total_value', models.PositiveIntegerField(default=0)),
                ('n_score', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('d_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('fk_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fk_product', models.ManyToManyField(related_name='producto_pedido', to='product.product')),
            ],
        ),
    ]
