from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {"place_holder_1":"Hello"}
    return render(request,"front_page.html",context= my_dict)