from django.shortcuts import render,redirect
from django.core.mail import send_mail
from src import settings
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"base.html")
    # return HttpResponse("<h1> hello </h1>")

def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        message = request.POST['message']
        # print(name,number,message)
        send_mail(
        'Query',
        'Name = ' + name + '\n' + 'Contact Number = ' + number + "\nMessage = " + message,
        settings.EMAIL_HOST_USER,
        ['b520031@iiit-bh.ac.in'],
        fail_silently=False,
        )
    return redirect("index")