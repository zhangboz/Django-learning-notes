from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StaffProfileInfo(models.Model):
    staff = models.OneToOneField(User)
    protfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)
    def __str__(self):
        return self.staff.username