from django.contrib import admin
from .models import Category, Blog

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('category_name', 'created_at', 'updated_at')
  search_fields = ('category_name', )

class BlogAdmin(admin.ModelAdmin):
  list_display = ('title','category', 'author', 'slug', 'status', 'is_featured', 'created_at', 'updated_at')
  prepopulated_fields = {'slug':('title',)}
  search_fields = ('id', 'title', 'category__category_name', 'status')
  list_editable = ('is_featured', )

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
