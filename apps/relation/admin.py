from django.contrib import admin
from .models import Departments, Staffs, Projects, Gloup, Person, Membership
# Register your models here.


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['name']


class StaffsAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_all_staffs_name']


class GloupAdmin(admin.ModelAdmin):
    list_display = ['name']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Staffs, StaffsAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Gloup, GloupAdmin)
admin.site.register(Person, PersonAdmin)
