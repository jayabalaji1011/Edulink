from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Assignment)

@admin.register(Sign_Up)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'user')  # Columns to display in admin
    search_fields = ('username', 'email')  # Searchable fields
    list_filter = ('user_type',)  # Add filters for user types

