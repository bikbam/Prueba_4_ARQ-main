from django.contrib import admin
from .models import EmpresaPyme, Producto,Categoria,Cliente,registro,venta,delivery,boleta,pagoPyme,comentarioProducto
# Register your models here.


admin.site.register(EmpresaPyme)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(registro)
admin.site.register(venta)
admin.site.register(delivery)
admin.site.register(boleta)
admin.site.register(pagoPyme)
admin.site.register(comentarioProducto)
#class ProductoAdmin(admin.ModelAdmin):
#    list_display = ["nombreProducto","descripcionProducto","categoriaProducto","activoProducto","PrecioProducto",'stock Procuto']


