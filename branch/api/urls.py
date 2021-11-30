from django.urls import path

from branch.api.views import BranchListAPIView

urlpatterns = [
    path('list', BranchListAPIView.as_view(), name='list'),

]
