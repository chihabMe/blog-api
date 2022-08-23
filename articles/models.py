import re
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from random import randint

# Create your models here.
User = get_user_model()
class ArticleManager(models.Manager):
    def get_queryset(self)  :
        return super().get_queryset().filter(publish=True)

class Article(models.Model):
    title = models.CharField(max_length=300)
    slug= models.SlugField(max_length=350,null=True,blank=True,unique=True)
    body = models.TextField()
    author = models.ForeignKey(User,related_name='articles',on_delete=models.CASCADE)

    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)
    ##managers
    tags = TaggableManager()
    objects= models.Manager()
    publishes = ArticleManager()


    def __str__(self) -> str:
        return self.title

@receiver(pre_save, sender=Article)
def pre_save_article(sender,instance,*args,**kwargs):
    count = Article.objects.filter(title=instance.title).count()
    if count!=0:
        instance.slug= slugify(instance.title)+"-"+str(count+1)
    

    
