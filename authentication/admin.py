from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    search_fields = ('fullname', 'number', 'email')
    list_display = ('fullname', 'number', 'email')
    filter_fields = ('is_staff', 'is_active')
    class Meta:
        model = User
        
        
        
admin.site.register(User, UserAdmin)