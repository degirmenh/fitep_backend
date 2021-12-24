from django.urls import path

from branch.api.views import BranchListAPIView, CategoryListAPIView

urlpatterns = [
    path('list', BranchListAPIView.as_view(), name='list'),
    path('category-list', CategoryListAPIView.as_view(), name='category-list'),

]
