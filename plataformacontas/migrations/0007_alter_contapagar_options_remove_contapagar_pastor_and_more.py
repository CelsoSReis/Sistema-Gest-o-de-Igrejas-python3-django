# Generated by Django 5.1.4 on 2025-02-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformacontas', '0006_alter_contapagar_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contapagar',
            options={},
        ),
        migrations.RemoveField(
            model_name='contapagar',
            name='pastor',
        ),
        migrations.AlterField(
            model_name='contapagar',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='contas/'),
        ),
        migrations.AlterField(
            model_name='contapagar',
            name='quantidade_parcelas',
            field=models.IntegerField(default=1),
        ),
    ]
