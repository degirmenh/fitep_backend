import datetime

from django.core.validators import ip_address_validator_map, validate_email
from django.db.models.fields import CharField

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
        fields = ['pk', 'username', 'first_name', 'last_name', 'birth_date', 'account_type',\
            'description', 'school_name', 'education_status', 'gender', 'identity_number', 'mobile_phone']


class AccountUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, allow_blank=True)
    last_name = serializers.CharField(max_length=255, allow_blank=True)
    birth_date = serializers.DateField()
    description = serializers.CharField(allow_blank=True)


    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class CoachSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)

    class Meta:
        model = Coach
        fields = ['account', 'courses']


class CoachUpdateSerializer(serializers.ModelSerializer):
    account = AccountUpdateSerializer(many=False)

    class Meta:
        model = Coach
        fields = ['account', 'courses']

    def update(self, instance, validated_data):
        account = validated_data.pop('account')
        account_serializer = AccountUpdateSerializer(instance = instance.account, data=account)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()
        return super(CoachUpdateSerializer, self).update(instance, validated_data)



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
            'identity_number', 'profile_photo', 'mobile_phone', 'birth_date', 'gender', 'description',\
                'education_status', 'school_name']

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
            date_joined=datetime.datetime.now(),
            gender=validated_data['gender'],
            description=validated_data['description'],
            education_status=validated_data['education_status'],
            school_name=validated_data['school_name']
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




class ProfilePhotoUpdateSerializer(serializers.Serializer):
    profile_photo = serializers.ImageField(required=True)

    def update(self, instance, validated_data):
        instance.profile_photo = validated_data.get('profile_photo', instance.profile_photo)
        instance.save()
