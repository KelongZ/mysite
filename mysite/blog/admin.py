from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_time',)
    list_display_links = ('title',)

admin.site.register(Article,ArticleAdmin)