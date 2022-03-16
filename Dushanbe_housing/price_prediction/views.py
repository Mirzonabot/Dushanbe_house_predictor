from django.shortcuts import render, HttpResponse
from price_prediction.forms import NewEntryForm

# Create your views here.

def index(request):
    form = NewEntryForm()

    context = {
        'form':form
    }

    return render(request,"index.html",context=context)
