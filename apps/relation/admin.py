from django.contrib import admin
from .models import Departments, Staffs, Projects
# Register your models here.


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['name']


class StaffsAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_all_staffs_name']


admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Staffs, StaffsAdmin)
admin.site.register(Projects, ProjectsAdmin)
