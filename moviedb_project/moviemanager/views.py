from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import NameForm
from .models import NameFormModel
import json, os, requests
from datetime import datetime
# Create your views here.
database = []
def moviemanagerView(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        #year_model = Year(request.POST)
        if form.is_valid():
            #Not initializing db here, instead storing cleaned data for manipulation
            cleanForm = form.cleaned_data
            print(cleanForm)
            print(type(cleanForm))
            #obj = NameFormModel.objects.create(**form.cleaned_data)
            movies_json = JsonResponse(cleanForm, safe = False)
            #Always have to futz with dates for one reason or another. This prevents the db from having datetime() instead of your actual date.
            cleanForm["date_watched_field"] = cleanForm["date_watched_field"].strftime("%m/%d/%Y")
            #Check to see if your db already exists, if it doesn't you need to do some more work. If it does you can just continue
            if os.path.exists('moviedatabase.json'):
                with open('moviedatabase.json') as outfile:
                    data = json.load(outfile)
            if not os.path.exists('moviedatabase.json'):
                data = []
            data.append(cleanForm)
            with open('moviedatabase.json','w') as outfile:
                json.dump(data,outfile)
            # This is just to show a response to the user. You can render another form here instead of the default form. This is your chance to return a templated list instead but this should get you on the right road.
            return HttpResponse(str(data))
            #return render (request, 'form.html',{'form':form})
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
