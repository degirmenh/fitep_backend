from django.db import models


class Course(models.Model):
    branch_id = models.IntegerField()

    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

