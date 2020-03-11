from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import MovieForm
from .models import MovieEntry, SearchFormModel
import json, os, requests
from datetime import datetime
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.
database = []

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        #year_model = Year(request.POST)
        if form.is_valid():
            #Not initializing db here, instead storing cleaned data for manipulation
            cleanForm = form.cleaned_data
            form.save()
            #obj = NameFormModel.objects.create(**form.cleaned_data)
            movies_json = JsonResponse(cleanForm, safe = False)
            #Always have to futz with dates for one reason or another. This prevents the db from having datetime() instead of your actual date.
            cleanForm["date_watched"] = cleanForm["date_watched"].strftime("%m/%d/%Y")
            #cleanForm["year_field"] = cleanForm["year_field"].strftime("%Y")
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
    elif request.method == "GET":
        form = MovieForm()
        return redirect (request, 'form.html',{'form':form})
    return redirect (request, 'form.html',{'form':form})


def home(request):
    movie_database = MovieEntry.objects.all()
    #return render (request, 'form.html',{'form':form,'entries':entries})
    return render(request, 'home.html',{'movie_database':movie_database})

'''def movie_edit(request, id):
    movie_id = int(id)
    try:
        movie_choice = NameFormModel.objects.get(id = movie_id)
    except NameFormModel.DoesNotExist:
        return redirect('moviemanager')
    if request.method == 'POST':
        form = NameForm(request.POST or None, instance = movie_id)
    if form.is_valid():
        form.save()
    return render(request, 'form.html',{'form':form})


def search(request):
    search = SearchFormModel(request.POST)
    entries = NameFormModel.objects.all().order_by('movie_title')
    return render (request, 'search.html',{'search':search,'entries':entries})'''

def about_page(request):
    page_tile = "About title"
    return render(request, "about.html",{"title":page_tile})

def contact_page(request):
    contact_title = "Contact title"
    return render(request, "contact.html",{"title":contact_title})
