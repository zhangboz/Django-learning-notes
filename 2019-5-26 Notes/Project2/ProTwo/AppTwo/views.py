from django.shortcuts import render
from django.http import HttpResponse

def Help(request):
    help_message = {'insert_me': "Here's Help."}
    return render(request,"appTwo/help.html",context=help_message)

# Create your views here.
def index(request):
    return HttpResponse("<em> My ProTwo</em>")