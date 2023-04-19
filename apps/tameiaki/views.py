from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.

def customers(request):
    #pull data from third party rest api
    response = requests.get('http://127.0.0.1:8280/customers')
    #convert reponse data into json
    data = response.json()
    context = {
        'customers': data,
    }
    print(context)
    return render(request, 'home.html', context)
    # customers = response.json()
    # customers = {'customers': customers}
    # print(customers)
    # return render(request, "home.html", {'customers': customers})
    
