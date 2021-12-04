from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from account.models import Account, Coach, Member


class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ['pk', 'username', 'first_name', 'last_name', 'birth_date', 'account_type']

    def update(self, instance, validated_data):
        return super(AccountSerializer, self).update(instance, validated_data)



class CoachSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)

    class Meta:
        model = Coach
        fields = ['account']

    def update(self, instance, validated_data):
        account = validated_data.pop('account')
        account_serializer = AccountSerializer(instance = instance.account, data=account)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()
        return super(CoachSerializer, self).update(instance, validated_data)


class MemberSerializer(serializers.ModelSerializer):
    
    account = AccountSerializer(many=False)

    class Meta:
        model = Member
        fields = ['account', ]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

        
