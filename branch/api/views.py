from rest_framework.generics import ListAPIView

from branch.api.serializers import BranchSerializer, CategorySerializer
from branch.models import Branch, Category


class BranchListAPIView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer



class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer