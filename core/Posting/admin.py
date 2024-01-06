from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_on")
    list_filter = ("status", "author")
    search_fields = ["title", "content", "created_on"]
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Post, PostAdmin)
