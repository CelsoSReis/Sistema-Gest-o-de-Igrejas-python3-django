# Generated by Django 5.1.4 on 2025-02-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformacontas', '0002_contapagar_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contapagar',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
