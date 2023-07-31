from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser, PermissionsMixin):
    ROLE = [
        ("user", "Пользователь"),
        ("admin", "Администратор")
    ]
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    phone = PhoneNumberField()
    email = models.EmailField(unique=True, null=False)
    role = models.CharField(max_length=5, choices=ROLE, default="member")
    image = models.ImageField(null=True, blank=True, upload_to="img")
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == "admin"

    @property
    def is_user(self):
        return self.role == "user"

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
