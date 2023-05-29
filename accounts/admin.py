from django.contrib import admin
from .models import Account
# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_name', 'last_name', 'password', 'email', 'last_login', 'date_joined', 'is_active']
    list_editable = ('first_name', 'last_name', 'email')
    readonly_fields = ['password', 'last_login', 'date_joined']
    ordering = ['-date_joined']

    def __str__(self):
        return self.first_name