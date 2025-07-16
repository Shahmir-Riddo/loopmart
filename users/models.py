from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import random
from django.conf import settings

# Create your models here.
     
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, unique=True, blank=True, null=True, validators=[RegexValidator(regex=r"^\d{11}", message="Phone Number must be 11 digits")])
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_vendor = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}"

    def generate_otp(self):
        self.otp = f"{random.randint(100000, 999999)}"
        self.save()
