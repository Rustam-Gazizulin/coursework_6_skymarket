from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager, UserRoles
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = PhoneNumberField(verbose_name='Телефон')
    is_active = models.BooleanField(default=False)
    image = models.ImageField(verbose_name='Аватар', null=True, blank=True)

    objects = UserManager()

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email' 

    # эта константа содержит список с полями, 
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
    
    @property
    def is_superuser(self):
        return self.is_admin
    
    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self):
        return self.is_admin

    def has_module_perms(self):
        return self.is_admin
