from django.shortcuts import render, redirect
from .models import form, url
from django.views.decorators.csrf import csrf_exempt
from .form import uploadform
import cloudinary
import os
import pymongo

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.


def index(request):

    return render(request, 'index.html')


@csrf_exempt
def submit(request):

    if request.POST:

        curr_form = uploadform(request.POST or None, request.FILES or None)

        if curr_form.is_valid():

            curr_form.save()

            imageurl = curr_form.instance.image.url
            name = curr_form.instance.name
            aadhaar = curr_form.instance.aadhaar


        
            print(os.path.join(BASE_DIR, imageurl[1:]).replace("\\","/"))
            imageurl=cloudinary.uploader.upload(
                os.path.join(BASE_DIR, imageurl[1:]).replace('\\','/'))

            insert = url.objects.create(
                imageurl=imageurl['url'], name=name, aadhaar=aadhaar)
            insert.save() 
        else:
            print(form.errors)

    return redirect('index')


def formview(request):

    return render(request, 'form.html')


def team(request):

    team=list(form.objects.all().values())

    for player in team:
        aadhaar=player['aadhaar']
        imageurl = url.objects.filter(aadhaar=aadhaar)[0].imageurl
        player['imageurl']=imageurl

    return render(request, 'team.html', {'team': team})


def showform(request):

    form=uploadform()

    return render(request, 'register.html', {'form': form})
