from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username','email')

class UserGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username','grade')


class FollowerSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only= True)
    followings = UserSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ('followers','followings')


class UserLikeArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','like_articles','like_users')