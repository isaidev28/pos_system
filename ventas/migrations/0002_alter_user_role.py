# Generated by Django 5.2.1 on 2025-05-20 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('ventas', 'Ventas')], default='ventas', max_length=20),
        ),
    ]
