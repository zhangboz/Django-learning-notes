from django import forms
from django.contrib.auth.models import User
from staff_data.models import StaffProfileInfo

class StaffForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username","email","password")


class StaffProfileInfoForm(forms.ModelForm):
    class Meta():
        model = StaffProfileInfo
        fields = ('protfolio_site','profile_pic')