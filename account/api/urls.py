from django.urls import path

from account.api.views import AccountListAPIView, CoachListApiView, MemberListApiView
from account.api.views import AccountUpdateAPIView, CoachUpdateAPIView
from account.api.views import UpdatePassword
from account.api.views import CreateAccountView, ProfilePhotoAPIView


urlpatterns = [
    path('list', AccountListAPIView.as_view(), name='list'),
    path('coach/list', CoachListApiView.as_view(), name='coach-list'),
    path('member/list', MemberListApiView.as_view(), name='member-list'),
    path('me', AccountUpdateAPIView.as_view(), name='account-update'),
    path('coach/me', CoachUpdateAPIView.as_view(), name='coach-update'),
    path('update_password', UpdatePassword.as_view(), name='update-password'),
    path('register', CreateAccountView.as_view(), name='register'),
    path('profile-photo', ProfilePhotoAPIView.as_view(), name='profile-photo'),
]

