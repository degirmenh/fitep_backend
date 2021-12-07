from rest_framework import serializers

from course.models import Course
from account.api.serializers import MemberSerializer


class CourseListSerializer(serializers.ModelSerializer):

    coach_name = serializers.ReadOnlyField(source='coach.account.first_name')
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'code', 'members', 'coach_name')

