# Generated by Django 5.1.7 on 2025-03-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0016_registroentrada_huella_validada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobro',
            name='vigencias_planes',
            field=models.ManyToManyField(blank=True, related_name='cobros_planes', to='WEB.vigenciaplan'),
        ),
    ]
