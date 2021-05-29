from django.contrib import admin

# Register your models here.
from blog.models import Category, Blog, Images

class BlogImageInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','image']
    list_filter = ['status']




class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category','image_tag','status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']
    inlines = [BlogImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','blog','image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Images,ImagesAdmin)
