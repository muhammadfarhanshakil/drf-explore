from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','niche','author','body', 'created_on', 'last_modified']
