# Generated by Django 5.1.4 on 2025-02-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformacontas', '0003_alter_contapagar_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='contapagar',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('paga', 'Paga')], default='pendente', max_length=10),
        ),
    ]
