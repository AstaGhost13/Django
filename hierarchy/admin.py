from django.contrib import admin

# Register your models here.
from .models import Floor, Department, Position, Custodiam


class FloorAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'status', 'description')
    search_fields = ( 'id',  'status', 'description')
    list_filter = ( 'id',  'status', 'description')


admin.site.register(Floor, FloorAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'id_floor', 'status', 'description', 'parent_description')
    search_fields = ( 'id', 'id_floor__description', 'status', 'description', 'parent__description')
    list_filter = ( 'id','id_floor', 'parent')
    autocomplete_fields = ['parent']  # Optional: Enables search for parent in the admin form

    def parent_description(self, obj):
        return obj.parent.description if obj.parent else None
    parent_description.short_description = 'Parent Description'

admin.site.register(Department, DepartmentAdmin)




class PositionAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'description', 'status', 'department')
    search_fields = ('id','description', 'department__description')
    list_filter = ('id', 'department')

admin.site.register(Position, PositionAdmin)



class CustodiamAdmin(admin.ModelAdmin):
    list_display = ('pkid','id', 'position', 'status','first_name', 'last_name')
    search_fields = ('pkid','id', 'position__description', 'first_name', 'last_name')
    list_filter = ('id', 'position')

admin.site.register(Custodiam, CustodiamAdmin)