import datetime

from django.core.validators import ip_address_validator_map, validate_email

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from account.models import Account, Coach, Member
from account.enums import AccountType


class ChoiceField(serializers.ChoiceField):
    
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)




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
        fields = ['account', 'courses']

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

        

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Account
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'account_type', \
            'identity_number', 'profile_photo', 'mobile_phone', 'birth_date']

    def validate(self, attr):
        validate_password(attr['password'])
        validate_email(attr['email'])
    
        

        return attr
    
    def validate_account_type(self, attr):
        print(attr)
        print([AccountType.MEMBER, AccountType.COACH])
        if attr in [AccountType.MEMBER, AccountType.COACH]:
            return attr
        else:
            return False
        

    def create(self, validated_data):
        account = Account.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            email=validated_data['email'],
            last_name=validated_data['last_name'],
            account_type=validated_data['account_type'],
            identity_number=validated_data['identity_number'],
            profile_photo=validated_data.get('profile_photo'),
            birth_date=validated_data['birth_date'],
            mobile_phone=validated_data['mobile_phone'],
            date_joined=datetime.datetime.now()
        )
        account.set_password(validated_data['password'])
        account.save()
        if validated_data['account_type'] == AccountType.COACH:
            coach = Coach.objects.create(account_id=account.id)
            coach.save()
        elif validated_data['account_type'] == AccountType.MEMBER:
            member = Member.objects.create(account_id=account.id)
            member.save()
        return account



