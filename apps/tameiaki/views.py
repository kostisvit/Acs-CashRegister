from django.shortcuts import render, redirect
import requests
import json
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Cash
from .forms import CashForm
from .export import CashExport,Export_data
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.http import JsonResponse
from .filters import CashFilter
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# API GET request Customers
@login_required
def customers(request):
    try:
        response = requests.get('http://host.docker.internal/customer-api') # http://127.0.0.1:8280/customer-api(without container)
        #convert reponse data into json
        data = json.loads(response.content)
        count = len(data)
        paginator = Paginator(data, 9) # 3 posts in each page
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
            'count':count
        }
    except requests.exceptions.RequestException as e:
        # Handle the error here
        error = {'message': f'Error connecting to external API: {str(e)}'}
        return JsonResponse(error, status=500)

    return render(request, "app/tameiaki/customer.html", context)


# LOAD all tameiakes
@method_decorator(login_required, name='dispatch')
class TameiakiFilterView(ListView):
    model = Cash
    template_name = 'app/tameiaki/tameiaki.html'
    paginate_by = 10

    def get_queryset(self):
        my_Filter = CashFilter(self.request.GET, queryset=super().get_queryset())
        return my_Filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_Filter'] = CashFilter(self.request.GET, queryset=self.get_queryset())
        context['query_params'] = self.request.GET.urlencode()
        return context


# Create new tameiaki entry
@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    model = Cash
    form_class = CashForm
    success_url = '/'
    template_name = 'app/new_records/tameiaki_new.html'
    

    def form_valid(self, form):
        response = requests.get('http://host.docker.internal/customer-api') # http://127.0.0.1:8280/customers-api(without container)
        api_id = response.json()
        instance = form.save(commit=False)
        instance.customer = api_id
        instance.customer = form.cleaned_data['customer']
        instance.save()
        return super().form_valid(form)


# Update view tameiaki
@method_decorator(login_required, name='dispatch')
class CashUpdateView(UpdateView):
    model = Cash
    form_class = CashForm
    success_url = '/'
    template_name = 'app/edit/tameiaki_edit.html'


    def form_valid(self, form):
        response = requests.get('http://host.docker.internal/customer-api') # http://127.0.0.1:8280/customers-api(without container)
        api_id = response.json()
        instance = form.save(commit=False)
        instance.customer = api_id
        instance.customer = form.cleaned_data['customer']
        instance.save()
        return super().form_valid(form)
    
