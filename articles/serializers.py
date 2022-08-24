import json
from rest_framework import serializers 
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    recommendations = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    author = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields  = ("title","author","body","created","updated","slug",'recommendations','image','introduction')
    def get_author(self,article):
        return article.author.username


    def create(self, validated_data):
        validated_data["author"]=self.context["request"].user
        return super().create(validated_data)
    def update(self, instance, validated_data):
        instance.body = validated_data.get("body") or instance.body
        instance.title = validated_data.get("title") or instance.title

        return super().update(instance, validated_data)
    def get_image(self,article):
        if not article.image:
            return None
        return self.context['request'].build_absolute_uri(article.image.url)
    def get_recommendations(self,article):
        slug = article.slug 
        object = Article.objects.get(slug=slug)
        similar_objects = object.tags.similar_objects()[:5]
        data=[]
        for object in similar_objects:
            item={
                'id':object.id,
                'title':object.title,
                'slug':object.slug,
            }
            if object.image : 
                item['image']=self.context['request'].build_absolute_uri(object.image.url) 

            data.append(item)

        return data


