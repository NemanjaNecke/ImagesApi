from django.contrib import admin
from . import models
from .models import Profile, Profilepic, ProfileAPIKey
from django.utils.html import format_html
# Register your models here.


@admin.register(models.Profilepic)
class PicAdmin(admin.ModelAdmin):
    def pic_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.pic.url))
    list_display = ('id', 'pic_tag', 'profile', 'selected')
    list_filter = ('profile',)


class ProfilePicInline(admin.TabularInline):
    model = Profilepic


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [ProfilePicInline, ]

    def pics(self, obj):
        pp = []
        for pic in obj.profilepic.all():
            return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format('http://127.0.0.1:8000/media/'+pic.__str__()))

    list_display = ('user', 'pics')


@admin.register(models.ProfileAPIKey)
class ProfileAPIKeyModelAdmin(admin.ModelAdmin):
    pass
