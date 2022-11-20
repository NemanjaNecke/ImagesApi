from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.


@admin.register(models.Images)
class AuthorAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.image.url))
    # def categories(self, obj):
        # return [category.name for category in obj.category.all()]

    def categories(self, obj):
        link1 = '<ul style="margin-left: 0.5em;">'
        for category in obj.category.all():
            link1 += '<li style="list-style-type: none;"><a href="/admin/images/images/?category__id__exact=%d">%s</a></li>' % (
                category.id, category.name)
        link1 += '</ul>'
        return format_html(link1)

    list_display = ('image_tag', 'title', 'id', 'status', 'author',
                    'slug', 'created', 'categories', )
    prepopulated_fields = {'slug': ('title',), }
    list_filter = ('category',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
# admin.site.register(models.Category)
