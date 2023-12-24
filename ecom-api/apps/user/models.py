# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from apps.commons.models import BaseModel

# from django.contrib.auth.models import (
#     User,
# )  # Using default user model for now. Later replace the auth token user foreignkey with the custom one


# class AuthToken(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     token = models.CharField(max_length=500)
#     expiry = models.DecimalField(max_digits=50, decimal_places=2)
#     created_on = models.DateTimeField(auto_now_add=True)


# class User(AbstractBaseUser):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     password = None
#     is_active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)  # a admin user; non super-user
#     admin = models.BooleanField(default=False)  # a superuser
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']  # Email & Password are required by default.
#
#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         """Does the user have a specific permission?"""
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         """Does the user have permissions to view the app `app_label`?"""
#         # Simplest possible answer: Yes, always
#         return True
#
#     @property
#     def is_staff(self):
#         """Is the user a member of staff?"""
#         return self.staff
#
#     @property
#     def is_admin(self):
#         """Is the user a admin member?"""
#         return self.admin
