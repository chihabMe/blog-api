from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    articles  = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User 
        fields =("username","email","articles")
    def get_articles(self,user):
        return user.articles.count()
