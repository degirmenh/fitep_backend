from django.db import models
from django.db.models.deletion import CASCADE


from branch.models import Branch
from account.models import Coach


CURRENCY_TYPES = [('try', "TRY"), ('usd', 'USD'), ('eur', 'EUR'), ('gbp', 'GBP')]


# Create your models here.
class PackageType(models.Model):
    SCALE_TYPE_CHOICES = (('hourly', 'Hourly'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly'))

    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    scale = models.CharField(choices=SCALE_TYPE_CHOICES, null=True, blank=True, max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'package_type'
        verbose_name = 'Package Type'
        verbose_name_plural = 'Package Types'


class Package(models.Model):
    branch = models.ForeignKey(Branch, on_delete=CASCADE, related_name='branch')
    coach = models.ForeignKey(Coach, on_delete=CASCADE, related_name='coach')
    package_type = models.ForeignKey(PackageType, on_delete=CASCADE, related_name='package_type')
    is_active = models.BooleanField(default=True)

    price = models.FloatField()
    currency = models.CharField(choices=CURRENCY_TYPES, null=True, blank=True, max_length=3)
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    user_count = models.PositiveIntegerField()


    class Meta:
        db_table = 'package'
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self) -> str:
        return f'{self.coach.account.full_name()} {self.package_type.name}'