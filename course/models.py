from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from branch.models import Branch
from account.models import Coach, Member


class Course(models.Model):
    code = models.CharField(max_length=35)
    name = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now=True)
    branch = models.ForeignKey(Branch, on_delete=CASCADE, related_name='courses')
    coach = models.ForeignKey(Coach, on_delete=CASCADE, related_name='courses')
    members = models.ManyToManyField(Member)


    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


    def __str__(self):
        return f'{self.code} {self.name}'

