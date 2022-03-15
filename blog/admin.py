from django.contrib import admin
from blog.models import Tag, Post
from blog.models import Tag, Post, Comment, AuthorProfile
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("published_at", "slug")

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(AuthorProfile)