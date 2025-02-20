from django.contrib import admin

from inventory.models import *
from resources.models import *
from hierarchy.models import *

# Register your models here.
class HardwareAdmin(admin.ModelAdmin):
    list_display = (
        'pkid', 
        'id', 
        'status',
        'product__description',
        'processor',
        'memory', 
        'tamanio', 
        'tipo_disco'
    )

admin.site.register(Hardware, HardwareAdmin)


class SoftwareAdmin(admin.ModelAdmin):
    list_display = (
        'pkid', 
        'id', 
        'status',
        'product__description',
        'version',
        'edition',
        'installation_date',
        'licenses',
        
    )
admin.site.register(Software, SoftwareAdmin)


class DisplayNameAdmin(admin.ModelAdmin):
    list_display = (
        'pkid', 
        'id', 
        'status',
        'name',
        'product__description',
     
    )
admin.site.register(DisplayName, DisplayNameAdmin)


class DateOperationAdmin(admin.ModelAdmin):
    list_display = (
        'pkid', 
        'id', 
        'status',
        'product__description',
        'date',
        'running_time',
    )
admin.site.register(DateOperation, DateOperationAdmin)


class  IpAssignationAdmin(admin.ModelAdmin):
    list_display = (
        'pkid', 
        'id', 
        'status',
        'product__description',
        'ip',
       
    )

admin.site.register(IpAssignation, IpAssignationAdmin) 



