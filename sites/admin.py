from django.contrib import admin
from .models import Sites

# Register your models here.

@admin.register(Sites)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'url')