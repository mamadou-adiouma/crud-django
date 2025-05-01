from django.contrib import admin

from crudapp.models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'couleur', 'categorie', 'prix', 'create_date')

admin.site.register(Products, ProductsAdmin)
