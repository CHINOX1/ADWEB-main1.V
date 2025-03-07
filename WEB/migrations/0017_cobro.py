# Generated by Django 5.1.5 on 2025-03-03 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0016_alter_pago_metodo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado')], default='pendiente', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cobros', to='WEB.registroempresas')),
                ('vigencia_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cobros', to='WEB.vigenciaplan')),
            ],
        ),
    ]
