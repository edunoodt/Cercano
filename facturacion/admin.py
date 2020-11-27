from django.contrib import admin
from .models import productos, personas, empresas, telefonos, facturas, items_factura

# Register your models here.

class productosAdm(admin.ModelAdmin):
    list_display = ('nombre','descripcion','cantidad','costo','margen','ubicacion','empresa')
    search_fields = ('nombre','costo','margen','ubicacion')

admin.site.register(productos, productosAdm)

class empresasAdm(admin.ModelAdmin):
    list_display = ('nombre','razon_social','cuit','tipo','direccion','ciudad','provincia','pais','codpost','bonificacion')
    search_fields = ('nombre','razon_social','cuit','tipo','direccion','ciudad','provincia','pais','codpost','bonificacion')

admin.site.register(empresas,empresasAdm)

class personasAdm(admin.ModelAdmin):
    list_display = ('apellido','nombre','cargo','mail','nacimiento','empleado','hijos','esposa','direccion','ciudad','provincia','pais','codpost','empresa')
    search_fields = ('apellido','nombre','cargo','mail','nacimiento','empleado','hijos','esposa','direccion','ciudad','provincia','pais','codpost')

admin.site.register(personas, personasAdm)

class telefonosAdm(admin.ModelAdmin):
    list_display = ('numero','tipo','persona')
    search_fields = ('numero','tipo','persona')

admin.site.register(telefonos,telefonosAdm)

class facturasAdm(admin.ModelAdmin):
    list_display = ('cliente','vendedor','fecha')
    search_fields = ('cliente','vendedor','fecha')

admin.site.register(facturas,facturasAdm)

class items_facturaAdm(admin.ModelAdmin):
    list_display = ('factura','producto','cantidad','precio')
    search_fields = ('factura','producto','cantidad','precio')

admin.site.register (items_factura,items_facturaAdm)


