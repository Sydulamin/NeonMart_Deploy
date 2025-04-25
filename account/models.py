from django.db import models

from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Profile(models.Model):
    Gender = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='user/', blank=True, null=True, default='default.png')
    address = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=Gender, blank=True, null=True)
    dob = models.CharField(max_length=10, null=True, blank=True, verbose_name='Date of Birth')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def user_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % self.image.url)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
