# Generated by Django 5.1.6 on 2025-02-13 14:53

import WEB.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registropermisos',
            options={},
        ),
        migrations.RemoveField(
            model_name='registropermisos',
            name='codigo',
        ),
        migrations.AlterField(
            model_name='registroempresas',
            name='rut',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='registroempresas',
            name='rut_representante',
            field=models.CharField(max_length=12, validators=[WEB.validators.validar_rut]),
        ),
        migrations.AlterField(
            model_name='registropermisos',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
