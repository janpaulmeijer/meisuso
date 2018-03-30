from django.contrib import admin
from accounts.models import UserProfile, Product, BlogItem
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(BlogItem)
