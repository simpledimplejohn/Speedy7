from django.shortcuts import render, redirect
from decouple import config, Csv
from django.http import HttpResponse, JsonResponse
from .services import Rapid7API
import requests

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

def new_variable(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        value = request.POST.get('value')

        if not all([name, description, value]):
            return JsonResponse({"status": "error", "message": "All fields are required!"})

        API_KEY = config('RAPID7_KEY')
        
        api_url = "https://us.rest.logs.insight.rapid7.com/query/variables"
        headers = {
            "Content-Type": "application/json",
            "X-Api-Key": API_KEY
        }
        data = {
            "variable": {
                "name": name,
                "description": description,
                "value": value
            }
        }

        try:
            response = requests.post(api_url, headers=headers, json=data)
            response_data = response.json()  # Extract JSON response content
            if response.status_code == 200:
                return JsonResponse({"status": "success", "message": "Variable created successfully!"})
            else:
                return JsonResponse({
                    "status": "error", 
                    "message": response_data.get("message", "Failed to create variable!"),
                    "response_code": response.status_code,
                    "details": response_data
                })
        except requests.RequestException as e:
            return JsonResponse({"status": "error", "message": str(e)})
    
    return render(request, 'new_variable.html')
