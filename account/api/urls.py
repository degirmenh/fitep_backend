from django.urls import path

from account.api.views import AccountListAPIView, CoachListApiView, MemberListApiView

urlpatterns = [
    path('list', AccountListAPIView.as_view(), name='list'),
    path('coach/list', CoachListApiView.as_view(), name='coach-list'),
    path('member/list', MemberListApiView.as_view(), name='member-list'),

]
