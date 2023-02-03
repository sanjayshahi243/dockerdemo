from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from demoApp.api.serializers import UserSerializer, AppModelSerializer

from django.contrib.auth.models import User
from demoApp.models import AppModel


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class DemoAppViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class Raise500(APIView):
    allowed_methods = ["get"]

    def get(self, request, format=None):
        """
        Raise 500 error
        """
        raise ValueError
        # usernames = [user.usernames for user in User.objects.all()]
        # return Response(usernames)

class CustomResponse(Response):
    pass