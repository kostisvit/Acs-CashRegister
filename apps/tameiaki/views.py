# from django.shortcuts import render
# from django.http import JsonResponse
# import requests
# # Create your views here.

# def customers(request):
#     #pull data from third party rest api
#     response = requests.get('http://127.0.0.1:8280/customers')
#     #convert reponse data into json
#     data = response.json()
#     data = {'data': data}
#     print(data)
#     return JsonResponse(data,safe=False, json_dumps_params={'ensure_ascii': False})


from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.utils.safestring import SafeString
import json
# Create your views here.
def customers(request):
    #pull data from third party rest api
    #response = requests.get('https://jsonplaceholder.typicode.com/users')
    response = requests.get('http://127.0.0.1:9999/customers')
    #convert reponse data into json
    data = json.loads(response.content)
    context = {
        'data': data,
    }
    print(customers)
    return render(request, "home.html", context)