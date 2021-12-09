from django.urls import path

from package.api.views import PackageTypesListView, PackageListView

urlpatterns = [
    path('package-types/list', PackageTypesListView.as_view(), name='package-type-list'),
    path('list', PackageListView.as_view(), name='list'),
    path('list/<int:coach_id>', PackageListView.as_view(), name='list-coach'),
    
]
