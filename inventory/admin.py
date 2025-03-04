from django.contrib import admin

from inventory.models import *
from hierarchy.models import *


# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'status', 'tipo', 'description')
    search_fields = ('description', 'tipo')
    list_filter = ('tipo', 'status')
admin.site.register(Brand, BrandAdmin)




class PrototypeAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'status', 'description', 'brand', 'tipo' )
    search_fields = ('description',)
    list_filter = ('status',)
    
admin.site.register(Prototype, PrototypeAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'codigo', 'id', 'status', 'description', 'serie', 'prototype')
    search_fields = ('description', 'serie')
    list_filter = ('status',)
admin.site.register(Product, ProductAdmin)


class ProductAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        'pkid', 
        'id',
        'status',
        'custodiam__first_name',
        'custodiam__last_name',
        'custodiam__position__description',
        'product__description',
        'product__serie',
        'product__prototype__description',
        'product__prototype__brand__description'
    )


admin.site.register(ProductAssignment, ProductAssignmentAdmin)