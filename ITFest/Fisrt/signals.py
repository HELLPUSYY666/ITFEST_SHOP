from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Customer


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'customer_profile'):
        Customer.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email
        )
