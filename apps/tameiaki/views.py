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
import requests
import json
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
# Create your views here.
def customers(request):
    #pull data from third party rest api
    #response = requests.get('https://jsonplaceholder.typicode.com/users')
    response = requests.get('http://127.0.0.1:8280/customers')
    #convert reponse data into json
    data = json.loads(response.content)
    paginator = Paginator(data, 12) # 3 posts in each page
    data = request.GET.get('page')
    try:
        data = paginator.page(data)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        data = paginator.page(paginator.num_pages)
    context = {
        'data': data,
        'page': data,
    }
    print(context)
    return render(request, "customer.html", context)
