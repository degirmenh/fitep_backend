from re import A
from rest_framework import serializers
import branch


from package.models import PackageType, Package, CURRENCY_TYPES
from account.api.serializers import CoachSerializer
from branch.api.serializers import BranchSerializer

class PackageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PackageType
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    package_type = PackageTypeSerializer()
    coach = CoachSerializer()
    branch = BranchSerializer()
    class Meta:
        model = Package
        fields = '__all__'



class PackageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


    def create(self, validated_data):
        package = Package.objects.create(
            branch=validated_data['branch'],
            coach=validated_data['coach'],
            package_type=validated_data['package_type'],
            is_active=True, price=validated_data['price'],
            currency=validated_data['currency'], user_count=validated_data['user_count'],
            description=validated_data['description']          
        )
        package.save()
        return package


class PackageUpdateSerializer(serializers.Serializer):
    branch_id = serializers.IntegerField()
    price = serializers.FloatField()
    currency = serializers.ChoiceField(choices=CURRENCY_TYPES, allow_blank=True)
    description = serializers.CharField(allow_blank=True)
    package_type_id = serializers.IntegerField()
    user_count = serializers.IntegerField()
    
    def update(self, instance, validated_data):
        instance.branch_id = validated_data.get('branch_id', instance.branch_id)
        instance.price = validated_data.get('price', instance.price)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.description = validated_data.get('description', instance.description)
        instance.package_type_id = validated_data.get('package_type_id', instance.package_type_id)
        instance.user_count = validated_data.get('user_count', instance.user_count)
        instance.save()
        return instance