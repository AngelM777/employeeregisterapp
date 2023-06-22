from django.contrib import admin

# Register your models here.
from .models import Position
admin.site.register(Position)

from .models import Employee
admin.site.register(Employee)