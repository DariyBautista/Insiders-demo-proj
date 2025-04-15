from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'access_level', 'author', 'created_at')
    list_filter = ('access_level',)
    search_fields = ('title', 'content')
