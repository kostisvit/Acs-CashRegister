from django.shortcuts import render
import requests
import json
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Cash
from .forms import CashForm


# API GET request
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
    return render(request, "app/tameiaki/customer.html", context)



# LOAD all tameiakes
def tameiaki(request):
    tameiaki = Cash.objects.all()
    context = {
        'data': tameiaki
    }
    return render(request, 'app/tameiaki/tameiaki.html', context)

from django.views.generic.edit import CreateView

class CreatePostView(CreateView):
    model = Cash
    form_class = CashForm
    template_name = 'app/new_records/tameiaki_new.html'