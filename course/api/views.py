from rest_framework.generics import ListAPIView

from course.api.serializers import CourseListSerializer
from course.models import Course


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer