from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics,mixins
from .serializers import UserProfileSerializer

User = get_user_model()

class UserListView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class=UserProfileSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)