from django.shortcuts import render, redirect
from decouple import config, Csv
from django.http import HttpResponse
from .services import Rapid7API

# Create your views here.
def index(request):
    information = {"name":"index"}
    return render(request, "index.html", information)

def tomato_view(request):
    context = {}
    if request.method == 'POST':
        # Extract the data directly from POST and add it to the context
        context['tomato_name'] = request.POST.get('tomato_name', '')
        context['tomato_description'] = request.POST.get('tomato_description', '')
        context['tomato_number'] = request.POST.get('tomato_number', 0)
        context['is_tomato'] = request.POST.get('is_tomato', 'off') == 'on'
    
    return render(request, 'tomato.html', context)

def variables_view(request):
    variables = Rapid7API.get_variables()
    return render(request, 'variables.html', {'variables': variables})