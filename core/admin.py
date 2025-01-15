from django.contrib import admin
from core.models import Autor, Categoria, Editora, Livro, Compra, ItensCompra


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
#admin.site.register(Compra)

class ItensInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)
