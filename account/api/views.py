from rest_framework.generics import ListAPIView

from account.models import Account, Coach, Member
from account.api.serializers import AccountSerializer, CoachSerializer, MemberSerializer


class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
        

class CoachListApiView(ListAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class MemberListApiView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer