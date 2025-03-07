"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from site import venv
from django.contrib.auth import views as auth_views
from django.urls import path


from WEB.views.config.views import sofware
from WEB.views.estadisticas.views import estadisticas
from WEB.views.sso.views import autenticacion, permisos
from WEB.views.tools.views import utilidades

from WEB.views.clientes.pagos.views import pagos
from WEB.views.clientes.empresa.views import empresas,planes

urlpatterns = [

 # Autenticación URLS:
    path('login/', autenticacion.login_view, name='login'),
    path('', auth_views.LoginView.as_view(template_name='login/login.html', redirect_authenticated_user=True), name='login'),
#redirige a la pagina principal despues de iniciar sesion:
    path('redirect_after_login/', autenticacion.redirect_after_login, name='redirect_after_login'),
#cerras sesion:
    path('logout/', autenticacion.logout_view, name='logout'),

#---------------------------------------------------------------------------------------------------------------------------------------------------#
#home URLS:
    #admin:
    path('admin_home/', autenticacion.admin_home, name='admin_home'),
    #supervisor:
    path('supervisor_home/<int:empresa_id>/', autenticacion.supervisor_home, name='supervisor_home'),
    #usuario:
    path('trabajador_home/', autenticacion.trabajador_home, name='trabajador_home'),
    #configuracion:
    path('configuracion_home/', autenticacion.configuracion_home, name='configuracion_home'),
    
#---------------------------------------------------------------------------------------------------------------------------------------------------#
# Sofware URLS:
    #crear admin:
    path('crear_admin/', sofware.crear_admin, name='crear_admin'),
    #crear supervisor:
    path('crear_supervisor/', sofware.crear_supervisor, name='crear_supervisor'),
    #crear trabajador:  
    path('crear_trabajador/', sofware.crear_trabajador, name='crear_trabajador'),
#---------------------------------------------------------------------------------------------------------------------------------------------------#
# Clientes  URLS:
    #lista de clientes:
    path('listar_clientes/', empresas.listar_clientes, name='listar_clientes'),
        #Crear Empresa:
            path('crear_empresa/', empresas.crear_empresa, name='crear_empresa'),
        #listar empresas eliminadas - recuperar - eliminar:
            path('eliminar_empresa/<int:pk>/', empresas.eliminar_empresa, name='eliminar_empresa'),
            path('empresas/eliminadas/', empresas.listar_empresas_eliminadas, name='listar_empresas_eliminadas'),
            path('empresa/recuperar/<int:id>/', empresas.recuperar_empresa, name='recuperar_empresa'),
        #desplliega los planes (servicios:)
            path('vigencia_planes/<int:pk>/', empresas.vigencia_planes, name='vigencia_planes'),
                #botones dentro del despliegue:
                    #generar boleta:
                        path('generar_boleta/<int:empresa_id>/', empresas.generar_boleta, name='generar_boleta'),
                    #boton editar :
                        path('editar_vigencia_plan/<int:plan_id>/', utilidades.editar_vigencia_plan, name='editar_vigencia_plan'),
#---------------------------------------------------------------------------------------------------------------------------------------------------#
        # boton para redirigir a pagos  :
        path('empresa/<int:empresa_id>/pagos/', pagos.gestion_pagos, name='gestion_pagos'),
            #desactivar pagos - servicios :
                #btn de actualziar pags de pendiente a aldia:
                    path('pago/actualizar/<int:pago_id>/', pagos.actualizar_estado_pago, name='actualizar_estado_pago'),
       
#---------------------------------------------------------------------------------------------------------------------------------------------------#

    #notficaiones :
    path('notificaciones/json/', pagos.notificaciones_json, name='notificaciones_json'),


    #Detalles Empresas:
    path('detalle_empresa/<int:pk>/', empresas.detalle_empresa, name='detalle_empresa'),

  


    #lista de planes:
    path('listar_planes/', planes.listar_planes, name='listar_planes'),
        #crear plan :
        path('crear_plan/', planes.crear_plan, name='crear_plan'), 

#---------------------------------------------------------------------------------------------------------------------------------------------------#
#estadisticas URLS:
    
    path('estadisticas/empresas/', estadisticas.estadisticas_empresas, name='estadisticas_empresas'),
    path('estadisticas/pagos/', estadisticas.estadisticas_pagos, name='estadisticas_pagos'),


#---------------------------------------------------------------------------------------------------------------------------------------------------#
#Permisos URLS:

    #Creaar permisos:
        path('crear_permiso/', permisos.crear_permiso, name='crear_permiso'),
    #listar permisos:
        path('lista_permisos/', permisos.lista_permisos, name='lista_permisos'),


#---------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------#
    path('empresa/<int:empresa_id>/pagos/', pagos.gestion_pagos, name='gestion_pagos'),
   

    # Otras rutas necesarias…
    path('empresa/<int:empresa_id>/cobros/registrar/', pagos.registrar_cobro, name='registrar_cobro'),
    path('empresa/<int:empresa_id>/cobro/<int:cobro_id>/actualizar/', pagos.actualizar_cobro, name='actualizar_cobro'),
    path('api/get_provincias/', utilidades.get_provincias, name='get_provincias'),
    path('api/get_comunas/',utilidades.get_comunas, name='get_comunas'),
   
    path('gestion-pagos/<int:empresa_id>/', pagos.gestion_pagos, name='gestion_pagos'),
    path('enviar-notificacion/<int:empresa_id>/', pagos.enviar_notificacion, name='enviar_notificacion'),
    
   
    
    
    
    
    

    ] 