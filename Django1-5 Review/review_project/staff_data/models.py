from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StaffProfileInfo(models.Model):
    staff = models.OneToOneField(User)
    # more attributes

    def __str__(self):
        return self.staff.username