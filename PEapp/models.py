from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, user_name, email, name, user_type, date_of_birth=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not user_name:
            raise ValueError('Users must have an user name')

        user = self.model(
            email=self.normalize_email(email),
            user_name = user_name,
            date_of_birth=date_of_birth,
            name=name,
            user_type=user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, email, name, password, **args):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(user_name, email, name,'O',password = password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    name = models.CharField(
        verbose_name='full name',
        max_length=255
    )
    user_name = models.CharField(
        verbose_name='user name',
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USER_TYPES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
        ('C', 'Pharmacist'),
        ('O', 'Other')
    )
    user_type = models.CharField(
        verbose_name='user type',
        max_length=1,
        default='P',
        choices=USER_TYPES
    )
    date_of_birth = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['name', 'email']

    class Meta:
        ordering = ["name"]
        verbose_name = 'User'

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Prescription(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=MyUser,related_name='prescription_user',on_delete=models.DO_NOTHING)
    content = models.TextField()

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('prescription-detail', args=[str(self.id)])

class MedicalRecord(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=MyUser,related_name='medicalrecord_user',on_delete=models.DO_NOTHING,)
    content = models.TextField()

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('medirecord-detail', args=[str(self.id)])