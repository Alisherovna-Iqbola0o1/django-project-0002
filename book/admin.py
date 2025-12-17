from django.contrib import admin
from .models import Author, Book, Store
# Register your models here.

@admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'nationality', 'age', 'total_books', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'nationality')

@admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'pages', 'price', 'cover', 'total_sold', 'in_stock', 'created_at')
    search_fields = ('author__first_name', 'author__last_name')

@admin.site.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'seller', 'total_sold_books', 'created_at')
    search_fields = ('name', 'address', 'seller__username')