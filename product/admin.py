from django.contrib import admin
from .models import Category,Product

# Register your models here.

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at', 'image_tag']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Product,ProductAdmin)