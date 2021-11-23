from django.db import models
from autoslug import AutoSlugField


class Branch(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        db_table = 'branch'
        verbose_name = 'Branch'
        verbose_name_plural = 'Branchs'

