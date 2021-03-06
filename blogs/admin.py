from django.contrib import admin
from .models import Blog, BlogImage, Category

# Register your models here.


class BlogImageAdmin(admin.ModelAdmin):
    pass


class BlogImageInline(admin.StackedInline):
    model = BlogImage
    #fields = ['image_tag']
    #readonly_fields = ['image_tag']
    max_num = 20
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline, ]

    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title')
    list_per_page = 25


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
