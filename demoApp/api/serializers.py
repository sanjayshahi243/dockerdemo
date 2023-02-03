from rest_framework import serializers

from django.contrib.auth.models import User
from demoApp.models import AppModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class AppModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppModel
        fields = '__all__'
