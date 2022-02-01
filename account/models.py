from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField

from branch.models import Branch
from account.enums import AccountType, GenderType, EducationStatus


class Account(AbstractUser):
    ACCOUNT_TYPE_CHOICES = ((AccountType.MEMBER, 'member'), (AccountType.COACH, 'coach'), (AccountType.ADMIN, 'admin'))
    GENDER_TYPE_CHOICES = ((GenderType.FEMALE, 'female'), (GenderType.MALE, 'male'))
    EDUCATION_TYPE_CHOICE = ((EducationStatus.PRIMARY, 'Primary'), (EducationStatus.SECONDARY, 'Secondary'), \
        (EducationStatus.HIGH, 'High'), (EducationStatus.COLLEGE, 'College'), (EducationStatus.SPORT_ACADEMY, 'Sport Academy'), \
            (EducationStatus.BACHELOR, 'Bachelor'), (EducationStatus.MASTER, 'Master'),(EducationStatus.DOCTORATE, 'Doctorate'))

    mobile_phone = models.CharField(max_length=25)
    email = models.EmailField(blank=True, unique=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='avatar/', blank=True, null=True)
    identity_number = models.CharField(max_length=25)
    account_type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPE_CHOICES, default=2)
    gender = models.PositiveSmallIntegerField(choices=GENDER_TYPE_CHOICES, blank=True, null=True, default=2)
    description = models.TextField(null=True, blank=True)
    education_status = models.PositiveSmallIntegerField(choices=EDUCATION_TYPE_CHOICE, null=False, blank=False, default=2)

    username = models.CharField(max_length=150)    
    school_name = models.CharField(max_length=255, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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
        return f'{self.account.full_name()}'



class Member(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'member'
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self) -> str:
        return f'{self.account.full_name()}'


