from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")



def staffpage(request):
    return render(request,"staff_data/staff_page.html")



def staffform(request):
    return render(request,"staff_data/staff_form.html")