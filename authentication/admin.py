from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields=["name", "email"]
    list_display = ['name','email', 'contactno', 'age']

# admin.site.register(User, UserAdmin)