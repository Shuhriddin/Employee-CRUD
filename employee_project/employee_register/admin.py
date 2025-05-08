from django.contrib import admin
from .models import Position, Employee
# Register your models here.

admin.site.register(Position)


@admin.register(Employee)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'emp_code', 'mobile', 'position']
    list_editable = ['position']
