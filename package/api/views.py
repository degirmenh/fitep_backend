from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response


from package.api.serializers import PackageTypeSerializer, PackageSerializer, PackageCreateSerializer
from package.models import PackageType, Package



class PackageTypesListView(ListAPIView):
    queryset = PackageType.objects.filter(is_active=True).all()
    serializer_class = PackageTypeSerializer
    


class PackageListView(ListAPIView):
    serializer_class = PackageSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def get_queryset(self):
        coach_id = self.kwargs.get('coach_id')
        if coach_id:
            queryset = Package.objects.filter(coach_id=coach_id, is_active=True).all()
        else:
            queryset = Package.objects.filter(is_active=True).all()
        return queryset
    


class PackageCreateView(CreateAPIView):
    model = Package.objects.all()
    serializer_class = PackageCreateSerializer