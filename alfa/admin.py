from django.contrib import admin
from .models import Floreria
# Register your models here.
class ComprarAdmin(admin.ModelAdmin):
    readonly_files=("fecha_creacion",)
    
admin.site.register(Floreria, ComprarAdmin)