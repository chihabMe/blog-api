from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
   summernote_fields = 'body'
   list_display = ("title","publish","author","updated","created","published",'introduction')
   prepopulated_fields = {
       "slug" :["title"]
    }

