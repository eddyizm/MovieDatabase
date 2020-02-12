from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import NameForm
from .models import NameFormModel
import json, os,requests
# Create your views here.
database = []
def moviemanagerView(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        #year_model = Year(request.POST)
        if form.is_valid():
            database.append(form.cleaned_data)
            print(database)
            print(type(database))
            #obj = NameFormModel.objects.create(**form.cleaned_data)
            form = NameForm()
            movies_json = JsonResponse(database, safe = False)
            with open('moviedatabase.json','w') as outfile:
                json.dump(database,outfile)
            return render (request, 'form.html',{'form':form})
    else:
        form = NameForm()
    return render (request, 'form.html',{'form':form})


def moviemanager(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form = NameForm()
            #return redirect('home:home')
            return render (request, 'form.html',{'form':form})
    else:
        form = NameForm()
    return render (request, 'form.html',{'form':form})

def about_page(request):
    page_tile = "About title"
    return render(request, "about.html",{"title":page_tile})

def contact_page(request):
    contact_title = "Contact title"
    return render(request, "contact.html",{"title":contact_title})
