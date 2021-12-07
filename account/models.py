from django.db import models
from django.contrib.auth.models import AbstractUser

from branch.models import Branch



class Account(AbstractUser):
    ACCOUNT_TYPE_CHOICES = ((1, 'member'), (2, 'coach'), (3, 'admin'))

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



class Coach(models.Model):
    
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    branches = models.ManyToManyField(Branch)
    
    class Meta:
        db_table = 'coach'
        verbose_name = 'Coach'
        verbose_name_plural = 'Coachs'

    def __str__(self) -> str:
        return f'{self.account.username}   {self.account.first_name}  {self.account.last_name}'


class Member(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'member'
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self) -> str:
        return f'{self.account.username}   {self.account.first_name}  {self.account.last_name}'



