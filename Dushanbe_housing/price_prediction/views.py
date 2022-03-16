from django.shortcuts import render, HttpResponse
from price_prediction.forms import InputParameters

# Create your views here.

def index(request):
    form = InputParameters()

    context = {
        'form':form
    }

    return render(request,"index.html",context=context)
