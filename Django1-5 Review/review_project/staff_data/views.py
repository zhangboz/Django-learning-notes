from django.shortcuts import render
from staff_data.models import StaffProfileInfo
from staff_data.forms import StaffForm, StaffProfileInfoForm
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    print("views.index is running")

    return render(request,"staff_data/index.html")



def staffpage(request):

    staff_dict = StaffProfileInfo.objects.all()
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


def staff_login(request):
    print("views.staff_login is running")

    if request.method == "POST":
        staffname = request.POST.get('username')
        password = request.POST.get('password')
        staff = authenticate(username = staffname, password = password)
        if staff:
            if staff.is_active:
                print("staff is active")
                login(request,staff)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Inactive")
        else:
            print("Failed Login Attempt")
            print("Username:{} and password:{}".format(staffname, password))
            return HttpResponse("Invalid username or password")
    else:
        print("rendering login.html")
        return render(request, "staff_data/login.html",{})

@login_required
def staff_logout(request):
    print("views.staff_logout is running")
    logout(request)
    return HttpResponseRedirect(reverse('index'))

