from WEB.models import *
from WEB.forms import *
from django.shortcuts import render, redirect
from WEB.decorators import permiso_requerido
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum



def estadisticas_empresas(request):
    empresas_por_mes = RegistroEmpresas.objects.annotate(
        mes=TruncMonth('fecha_ingreso')
    ).values('mes').annotate(
        total=Count('id')
    ).order_by('mes')
    context = {
        'empresas_por_mes': list(empresas_por_mes),
    }
    return render(request, 'side_menu/estadisticas/empresas/empresas.html', context)

def estadisticas_pagos(request):
    pagos_por_mes = Pago.objects.annotate(
        mes=TruncMonth('fecha_pago')
    ).values('mes').annotate(
        cantidad=Count('id'),
        monto_total=Sum('monto')
    ).order_by('mes')
    context = {
        'pagos_por_mes': list(pagos_por_mes),
    }
    return render(request, 'side_menu/estadisticas/pagos/pagos.html', context)



