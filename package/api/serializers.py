from rest_framework import serializers

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