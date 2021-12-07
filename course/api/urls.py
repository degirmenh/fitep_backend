from django.urls import path

from course.api.views import CourseListAPIView

urlpatterns = [
    path('list', CourseListAPIView.as_view(), name='list'),

]
