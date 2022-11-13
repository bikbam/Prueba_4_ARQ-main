from django.contrib import admin
from .models import EmpresaPyme, Producto,Categoria,Cliente
# Register your models here.


admin.site.register(EmpresaPyme)
admin.site.register(Categoria)
admin.site.register(Producto)
#class ProductoAdmin(admin.ModelAdmin):
#    list_display = ["nombreProducto","descripcionProducto","categoriaProducto","activoProducto","PrecioProducto",'stock Procuto']


