from tameiaki.models import Cash
    
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