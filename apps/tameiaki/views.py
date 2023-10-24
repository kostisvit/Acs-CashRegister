import logging
import requests
import json
from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Cash,UploadFile
from .forms import CashForm, ClientForm, FileUploadForm, CashUpdateForm
from .export import Export_data,export_data_as_excel,CashExport
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, FormView
from django.http import JsonResponse
from .filters import CashFilter,FileFilter
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# API GET request Customers
@login_required
def customers(request):
    try:
        response = requests.get('http://host.docker.internal:8280/customer-api') # http://127.0.0.1:8280/customer-api(without container)
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
    
    def get(self, request, *args, **kwargs):
        logger.info(f'Accessing the {self.model.__name__} list view.')
        return super().get(request, *args, **kwargs)


# Create new tameiaki entry
@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    model = Cash
    form_class = CashForm
    success_url = reverse_lazy('tameiaki')
    template_name = 'app/new_records/tameiaki_new.html'
    
    def form_valid(self, form):
        try:
            response = requests.get('http://host.docker.internal:8280/customer-api') # http://127.0.0.1:8280/customers-api(without container)
            api_id = response.json()
            instance = form.save(commit=False)
            instance.customer = api_id
            instance.customer = form.cleaned_data['customer']
            logger.info('Record created succesfully')
            instance.save()
            return super().form_valid(form)
        except Exception as e:
            logger.exception('An error occurred in the CreateView: %s', str(e))

    def form_invalid(self, form):
        logger.error('Record creation process encountered an error.')
        return super().form_invalid(form)


# Update view tameiaki
@method_decorator(login_required, name='dispatch')
class CashUpdateView(UpdateView):
    model = Cash
    form_class = CashUpdateForm
    success_url = '/'
    template_name = 'app/edit/tameiaki_edit.html'

    
    def form_valid(self, form):
        obj = self.get_object()
        try:
            response = requests.get('http://host.docker.internal:8280/customer-api') # http://127.0.0.1:8280/customers-api(without container)
            api_id = response.json()
            instance = form.save(commit=False)
            instance.customer = api_id
            instance.customer = form.cleaned_data['customer']
            instance.save()
            logger.info('UpdateView successfully updated object with ID %d and data: %s', obj.id, obj.__dict__)
            return super().form_valid(form)
        except Exception as e:
            logger.exception('An error occurred in the UpdateView: %s', str(e))



#Client API Post
@method_decorator(csrf_exempt, name='dispatch')
class CustomerFormView(FormView):
    template_name = 'app/new_records/customer_new.html'
    form_class = ClientForm
    success_url = '/'

    def form_valid(self, form):
        api_url = 'http://host.docker.internal:8280/api/customer-new'
        data = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'company_name': form.cleaned_data['company_name'],
            'company_type': form.cleaned_data['company_type'],
            'company_address': form.cleaned_data['company_address'],
            'company_afm': form.cleaned_data['company_afm'],
            'company_email': form.cleaned_data['company_email'],
            'phone_number': form.cleaned_data['phone_number']

        }
        response = requests.post(api_url, data=data)

        if response.status_code == 200:
            return super().form_valid(form)
        else:
            form.add_error(None, 'Failed to submit the form. Please try again.')
            return self.form_invalid(form)



#Upload file
class FileUploadView(FormView):
    model = UploadFile
    template_name = 'app/tameiaki/upload_file.html'
    form_class = FileUploadForm
    success_url = '/'

    def form_valid(self, form):
        logger.info('File upload process started.')
        file = self.request.FILES.getlist('file')
        for uploaded_file in file:
            instance = UploadFile(file=uploaded_file)

        response = requests.get('http://host.docker.internal:8280/customer-api') # http://127.0.0.1:8280/customers-api(without container)
        api_id = response.json()
        instance = form.save(commit=False)
        instance.customer = api_id
        instance.customer = form.cleaned_data['customer']
        instance.save()

        logger.info('File "%s" uploaded successfully.', uploaded_file.name)
        logger.info('File size: %s bytes', uploaded_file.size)

        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Log that the file upload process encountered an error
        logger.error('File upload process encountered an error.')
        return super().form_invalid(form)




# Display files
class FileListView(ListView):
    model = UploadFile
    template_name = 'app/tameiaki/files.html'
    success_url = '/'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(file__exact='')
        return queryset
    
    def get(self, request, *args, **kwargs):
        logger.info(f'Accessing the {self.model.__name__} filelist view.')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        my_Filter = FileFilter(self.request.GET, queryset=super().get_queryset())
        return my_Filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_Filter'] = FileFilter(self.request.GET, queryset=self.get_queryset())
        context['query_params'] = self.request.GET.urlencode()
        return context
