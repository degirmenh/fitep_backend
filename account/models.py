from django.db import models
from django.contrib.auth.models import AbstractUser

from branch.models import Branch
from account.helpers import AccountType


class Account(AbstractUser):
    ACCOUNT_TYPE_CHOICES = ((AccountType.MEMBER, 'member'), (AccountType.COACH, 'coach'), (AccountType.ADMIN, 'admin'))

    mobile_phone = models.CharField(max_length=25)
    birth_date = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='avatar/', blank=True, null=True)
    identity_number = models.CharField(max_length=25)
    account_type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPE_CHOICES, null=True, blank=True)



    class Meta:
        db_table = 'fitep_account'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name}' 
    
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'{self.full_name()}'



class Coach(models.Model):
    
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    branches = models.ManyToManyField(Branch)
    
    class Meta:
        db_table = 'coach'
        verbose_name = 'Coach'
        verbose_name_plural = 'Coachs'

    def __str__(self) -> str:
        return super().__str__()



class Member(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'member'
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self) -> str:
        return super().__str__()


