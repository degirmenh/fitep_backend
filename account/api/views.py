from account.api.serializers import ChangePasswordSerializer, RegisterSerializer, ProfilePhotoUpdateSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


from account.models import Account, Coach, Member
from account.api.serializers import AccountSerializer, CoachSerializer, MemberSerializer, AccountUpdateSerializer, \
    CoachUpdateSerializer


class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
        

class CoachListApiView(ListAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class MemberListApiView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class AccountUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountUpdateSerializer
    queryset = Account.objects.all()

    def get_object(self):
       queryset = self.get_queryset()
       obj = get_object_or_404(queryset, id = self.request.user.id)
       return obj
    
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)
    

class CoachUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CoachUpdateSerializer
    queryset = Coach.objects.all()

    def get_object(self):
       queryset = self.get_queryset()
       obj = get_object_or_404(queryset, account_id = self.request.user.id)
       return obj
    
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)


class UpdatePassword(APIView):
    permission_class = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {'old_password': request.data['old_password'], 'new_password': request.data['new_password']}

        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            if  not self.object.check_password(old_password):
                return Response({"old_password": "wrong password"}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# Create Account
class CreateAccountView(CreateAPIView):
    model = Account.objects.all()
    serializer_class = RegisterSerializer


# Profile Photo

class ProfilePhotoAPIView(APIView):
    permission_class = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {'profile_photo': request.FILES.get('profile_photo')}
        serializer = ProfilePhotoUpdateSerializer(data=data)
        if serializer.is_valid():
            self.object.profile_photo = request.FILES.get('profile_photo')
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not self.object:
            return Response("User can not found", status = status.HTTP_404_NOT_FOUND)
        data = {'profile_photo': self.object.profile_photo.url}
        return Response(data)


