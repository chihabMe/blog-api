from rest_framework import serializers 
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields  = ("title","author","body","created","updated","slug")
    def get_author(self,article):
        return article.author.username


    def create(self, validated_data):
        validated_data["author"]=self.context["request"].user
        return super().create(validated_data)
    def update(self, instance, validated_data):
        instance.body = validated_data.get("body") or instance.body
        instance.title = validated_data.get("title") or instance.title

        return super().update(instance, validated_data)