import os

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.managers import CustomUserManager
from utils.data_validatiors import process_image, validate_file_size, validate_image_file, validate_phone_number


def customer_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f'user-{instance.id}{extension}'

    return os.path.join('uploads/user/', filename)


class BaseProfile(models.Model):
    T_SHIRT_SIZE_CHOICES = [
        ('XXS', 'Very Extra Small'),
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
        ('XXXL', 'Very Extra Extra Large'),
    ]

    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50, null=False)

    firstNameEng = models.CharField(max_length=50, null=False, blank=False)
    lastNameEng = models.CharField(max_length=50, null=False, blank=False)

    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], null=False)
    dateOfBirth = models.DateField(null=True, blank=True)
    tShirtSize = models.CharField(
        max_length=5, choices=T_SHIRT_SIZE_CHOICES, null=True
    )

    country = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)

    phoneNumber = models.CharField(
        _('phone number'),
        max_length=20,
        null=False,
        validators=[validate_phone_number],
    )

    sportsClub = models.CharField(max_length=100, null=True)

    emergencyContactName = models.CharField(max_length=100, null=False)
    emergencyContactPhone = models.CharField(
        _('phone number'),
        null=False,
        max_length=20,
        validators=[validate_phone_number],
    )


    class Meta:
        abstract = True


class CustomUser(BaseProfile, AbstractBaseUser, PermissionsMixin):
    USER = 'user'
    ORGANIZER = 'organizer'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (USER, 'User'),
        (ORGANIZER, 'Organizer'),
        (ADMIN, 'Administrator'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=customer_image_file_path,
        max_length=255,
        validators=[validate_image_file, validate_file_size]
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.avatar:
            process_image(self.avatar, size=(300, 300))
        super().save(*args, **kwargs)

