from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from package.api.serializers import PackageTypeSerializer, PackageSerializer, PackageCreateSerializer, \
    PackageUpdateSerializer
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


class PackageUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PackageUpdateSerializer
    queryset = Package.objects.all()


    def get_queryset(self):
        package_id = self.kwargs.get('package_id')
        if package_id:
            queryset = Package.objects.filter(pk=package_id)
        return queryset


    def get_object(self):
       queryset = self.get_queryset()
       obj = get_object_or_404(queryset, pk = self.kwargs.get('package_id'))
       return obj
    
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)