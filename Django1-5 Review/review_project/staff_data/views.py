from django.shortcuts import render
from staff_data.models import StaffProfileInfo
from staff_data.forms import StaffForm, StaffProfileInfoForm
from django import forms

# Create your views here.
def index(request):
    return render(request,"staff_data/index.html")



def staffpage(request):

    staff_dict = StaffProfileInfo.objects.all()
    print(staff_dict)

    return render(request,"staff_data/staff_page.html", context = {"staff_data":staff_dict})



def staffform(request):
    registered = False
    if request.method =="POST":
        form_dict_1 = StaffForm(data = request.POST)
        form_dict_2 = StaffProfileInfoForm(data = request.POST)

        if form_dict_1.is_valid() and form_dict_2.is_valid():
            staff = form_dict_1.save()
            staff.set_password(staff.password)
            staff.save()
            profile = form_dict_2.save(commit = False)
            profile.staff = staff
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(form_dict_1.errors, form_dict_2.errors)
    else:
        form_dict_1 = StaffForm()
        form_dict_2 = StaffProfileInfoForm()
    return render(request,"staff_data/staff_form.html",{'form':form_dict_1 , 'profile_form':form_dict_2,'registered':registered})
