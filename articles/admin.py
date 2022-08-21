from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","publish","author","updated","created","published")
    prepopulated_fields = {
       "slug" :["title"]
    }

