import re

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, name: str, phone: str, password: str) -> 'User':
        if not self.model.check_email(email):
            raise TypeError('must have email.')

        if not name:
            raise ValueError('must have name')

        if not self.model.check_phone(phone):
            raise ValueError('must have phone')

        if not password:
            raise ValueError('must have password')

        user = User.objects.create(
            email=email,
            name=name,
            phone=phone,
            password=make_password(password),
        )

        return user

    def create_superuser(self, email: str, name: str, phone: str, password: str) -> 'User':
        if not self.model.check_email(email):
            raise ValueError('must have email.')

        if not name:
            raise ValueError('must have name')

        if not self.model.check_phone(phone):
            raise ValueError('must have phone')

        if not password:
            raise ValueError('must have password')

        superuser = User.objects.create(
            email=email,
            name=name,
            phone=phone,
            password=make_password(password),
        )

        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=13)

    is_active = models.BooleanField(default=False)
    is_freeze = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}({self.email})'

    @staticmethod
    def check_phone(phone: str) -> bool:
        return re.compile('\d{3}-\d{3,4}-\d{4}').match(phone) is not None

    @staticmethod
    def check_email(email: str) -> bool:
        return re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$').match(email) is not None
