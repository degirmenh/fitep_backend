from rest_framework import serializers
from account.models import Account, Coach, Member


class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'birth_date', 'account_type']



class CoachSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)

    class Meta:
        model = Coach
        fields = ['account']


class MemberSerializer(serializers.ModelSerializer):
    
    account = AccountSerializer(many=False)

    class Meta:
        model = Member
        fields = ['account', ]