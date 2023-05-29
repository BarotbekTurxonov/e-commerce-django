from django.contrib import admin
from .models import Category
# Register your models here.
@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug' : ('category_name',)}
