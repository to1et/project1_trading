from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, nickname=None, username=None, profile_image=None, phonenumber=None, address=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname = nickname,
            username = username,
            profile_image = profile_image,
            phonenumber = phonenumber,
            address = address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname=None, username=None, profile_image=None, phonenumber=None, address=None, password=None):
        user = self.create_user(
            email,
            password=password,
            nickname = nickname,
            username = username,
            profile_image = profile_image,
            phonenumber = phonenumber,
            address = address,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True,)
    nickname = models.CharField(max_length=24, default=None, null=True, blank=True, unique=True)
    username = models.CharField(max_length=24, default=None, null=True, blank=True)
    profile_image = models.TextField(default=None, null=True, blank=True)
    phonenumber = models.IntegerField(default=None, null=True, unique=True, blank=True)
    address = models.TextField(default=None, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
