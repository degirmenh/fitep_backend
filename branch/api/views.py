from rest_framework.generics import ListAPIView

from branch.api.serializers import BranchSerializer
from branch.models import Branch


class BranchListAPIView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer