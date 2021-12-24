from django.db import models
from autoslug import AutoSlugField

from django.db.models.deletion import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Branch(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='branches', null=True, blank=True)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'branch'
        verbose_name = 'Branch'
        verbose_name_plural = 'Branchs'



