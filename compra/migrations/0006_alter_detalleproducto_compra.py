# Generated by Django 5.1.1 on 2024-10-24 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0005_compra_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleproducto',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='compra.compra'),
        ),
    ]
