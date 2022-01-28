from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Book)

#customized with decorator
#this will help us to customize what fields will be available when
# someone clicks on a book object in admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields customized what fields will be available when
    # someone clicks on a book object in admin
    fields = ['title', 'description']
    #list_display customizes what people see when they see a list of Book objects
    list_display = ['title', 'description', 'price']
    #makes "published" available as a filter
    list_filter = ['published']
    #allows for search bar to include the fields in this list
    search_fields = ['title', 'description']