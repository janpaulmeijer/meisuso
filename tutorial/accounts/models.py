from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default = '', null=True)
    country = models.CharField(max_length=100, default = '', null=True)
    state = models.CharField(max_length=100, default = '', null=True)
    city = models.CharField(max_length=100, default = '', null=True)
    adress = models.CharField(max_length=100, default = '', null=True)
    postcode = models.CharField(max_length=100, default = '', null=True)
    website = models.URLField(default = '', null=True)
    phone = models.IntegerField(default = 0, null=True)
    company = models.CharField(max_length=100, default = '', null=True)
    hdyhau = models.CharField(max_length=1000, default = '', null=True)
    customer_role = (
        ('B', 'Buyer'),
        ('P', 'Producer'),
        ('O', 'Other'),
    )
    role = models.CharField(max_length=1, choices=customer_role, default='', null=True)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    product_name = models.CharField(max_length=100, default = '')
    price = models.IntegerField(default = 0)
    CAT = (
        ('F', 'Fruit'),
        ('V', 'Vegetable'),
    )
    category = models.CharField(max_length=1, choices=CAT, default = '')
    season = models.CharField(max_length=100, default = '')
    description = models.CharField(max_length=100, default = '')
    unit = models.CharField(max_length=100, default = '')

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.product_name
