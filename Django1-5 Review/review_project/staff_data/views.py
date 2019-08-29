from django.shortcuts import render
from staff_data.models import StaffProfileInfo
from staff_data.forms import StaffForm
from django import forms

# Create your views here.
def index(request):
    return render(request,"staff_data/index.html")



def staffpage(request):

    staff_dict = StaffProfileInfo.objects.all()
    print(staff_dict)

    return render(request,"staff_data/staff_page.html", context = {"staff_data":staff_dict})



def staffform(request):
    form_dict = StaffForm()
    if request.method =="POST":
        form_dict = StaffForm(request.POST)
        # if form.is_valid():
        #     print(form)
    return render(request,"staff_data/staff_form.html",{'form':form_dict})
