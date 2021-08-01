from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    

    return render(request, "home.html", {})

'''if request.user.is_superuser == True:
        return HttpResponse('You are super user.')
    else:
        return HttpResponse('Fuck you.')'''