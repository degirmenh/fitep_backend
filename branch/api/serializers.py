from rest_framework import serializers

from branch.models import Branch, Category



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        
class BranchSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Branch
        fields = ('name', 'slug', 'category', 'is_active')


