from re import A
from rest_framework import serializers
import branch


from package.models import PackageType, Package
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