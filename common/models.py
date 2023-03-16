from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, username, phonenumber, address, profile_image=None, password=None):
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

    def create_superuser(self, email, nickname, username, phonenumber, address, profile_image=None, password=None):
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
    # User모델에 넣고싶은 field
    #  blank=True 값을 넣으면 폼 항목에서 필수 항목이 아니게 된다.
    #  null=True 값은 폼이 아닌 곳에서 필수가 아니게 된다.
    email = models.EmailField(verbose_name='email', max_length=255, unique=True,)
    nickname = models.CharField(max_length=24, default=None,  unique=True)
    username = models.CharField(max_length=24, default=None)
    profile_image = models.TextField(default=None, null=True, blank=True)
    phonenumber = models.TextField(default=None, unique=True)
    address = models.TextField(default=None)
    is_superuser = models.BooleanField(default=False)

    # User모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()


    USERNAME_FIELD = 'email'
    # 필수로 입력해야 하는 field
    REQUIRED_FIELDS = ['nickname', 'username', 'phonenumber', 'address']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
