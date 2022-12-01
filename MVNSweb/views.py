from django.http import HttpResponse
from django.shortcuts import render
from .forms import ReadingForm
from .models import Reading

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, "MVNSweb\index.html", {'page_title': 'Home'})

def view(request, *args, **kwargs):
    reading = Reading.objects.all()
    context = {
        'Reading' : reading,
        'page_title': 'View',
    }
    return render(request, "MVNSweb\mvns_view.html", context)

def add_data(request, *args, **kwargs):
    addForm = ReadingForm(request.POST or None)
    if addForm.is_valid():
        addForm.save()
        addForm = ReadingForm()
    context = {
        'page_title': 'Add',
        'addForm': addForm
    }
    return render(request, "MVNSweb\mvns_add_data.html", context)

def edit_data(request, *args, **kwargs):
    return render(request, "MVNSweb\mvns_edit_data.html", {'page_title': 'Edit'})



