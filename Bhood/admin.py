from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'cont',)
    list_display_links = ('title',)

class CateAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_display_links = ('category',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

class PredlozkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'cont',)
    list_display_links = ('title',)

class AdminComments(admin.ModelAdmin):
    list_display = ('author', 'comment',)
    list_display_links = ('comment',)

class RateAdmin(admin.ModelAdmin):
    list_display = ('post', 'rate')
    list_display_links = ('post', 'rate')

admin.site.register(Post, PostAdmin)
admin.site.register(Cate)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Predlozka, PredlozkaAdmin)
admin.site.register(Comments, AdminComments)
admin.site.register(RatePost, RateAdmin)

