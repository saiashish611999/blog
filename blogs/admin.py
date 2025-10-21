from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('category_name', 'created_at', 'updated_at')
  search_fields = ('category_name', )

# Register your models here.
admin.site.register(Category, CategoryAdmin)
