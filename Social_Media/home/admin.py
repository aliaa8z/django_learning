from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'created']
    list_filter = ['created']
    search_fields = ['slug']
    prepopulated_fields = {'slug': ['body']}
    raw_id_fields = ['user']


# admin.site.register(Post, PostAdmin)