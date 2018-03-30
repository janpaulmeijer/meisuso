from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from geopy.geocoders import Nominatim


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default = '', null=True, blank=True)
    country = models.CharField(max_length=100, default = '', null=True, blank=True)
    state = models.CharField(max_length=100, default = '', null=True, blank=True)
    city = models.CharField(max_length=100, default = '', null=True, blank=True)
    adress1 = models.CharField(max_length=1000, default = '', null=True, blank=True)
    adress2 = models.CharField(max_length=1000, default = '', null=True, blank=True)
    postcode = models.CharField(max_length=100, default = '', null=True, blank=True)
    website = models.URLField(default = '', null=True, blank=True)
    phone = models.IntegerField(default = 0, null=True, blank=True)
    company = models.CharField(max_length=100, default = '', null=True, blank=True)
    hdyhau = models.CharField(max_length=1000, default = '', null=True, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null = True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null = True, blank=True)
    customer_role = (
        ('Buyer', 'Buyer'),
        ('Producer', 'Producer'),
        ('Other', 'Other'),
    )
    role = models.CharField(max_length=8, choices=customer_role, default='', null=True, blank=True)

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

class BlogItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    title = models.CharField(max_length=100, default = '', null=True, blank=True)
    description = models.TextField(max_length=10000, default = '', null=True, blank=True)

    def __str__(self):
        return self.title
