from django.contrib import admin
from .models import Post
# Register your models here.
# admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','create_on')
    list_filter = ('status',)
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)