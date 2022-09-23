from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.

@admin.register(models.Images)
class AuthorAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.image.url))

    def category_link(self, obj):
        return format_html('<a href="/admin/images/images/?category__id__exact=%d">%s</a>' % (obj.category_id, obj.category))

    
    list_display = ('image_tag', 'title', 'id', 'status', 'slug', 'created', 'category_link')
    prepopulated_fields = {'slug':('title',),}
    list_filter = ('category',)

    
admin.site.register(models.Category)