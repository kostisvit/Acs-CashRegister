from tameiaki.models import Cash, UploadFile
from .views import get_api_customers_count,get_api_offline_customers_count
    
def cash_count(request):
    return {
        'cash': Cash.objects.all().count()
    }

def cash_count_online(request):
    return {
        'cash_online': Cash.objects.filter(status=True).count()
    }

def cash_count_offline(request):
    return {
        'cash_offline': Cash.objects.filter(status=False).count()
    }

def file_count(request):
    return {
        'file_count': UploadFile.objects.all().count()
    }

def voucher_count(request):
    return {
        'voucher_count': Cash.objects.filter(voucher=True).count()
    }

def pos_connection_count(request):
    return {
        'pos_connection_count': Cash.objects.filter(pos_connect=True).count()
    }


def api_filtered_customers_count(request):
    count = get_api_customers_count()
    return {'api_filtered_customers_count': count}


def api_filtered_offline_customers_count(request):
    count = get_api_offline_customers_count()
    return {'api_filtered_offline_customers_count': count}