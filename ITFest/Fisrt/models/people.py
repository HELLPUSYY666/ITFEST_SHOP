from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from ITFest.Fisrt.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=User)
    def create_customer_profile(sender, instance, created, **kwargs):
        if created and not hasattr(instance, 'customer'):
            Customer.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name,
                                    email=instance.email)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
