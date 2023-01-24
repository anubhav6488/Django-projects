from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from controler.models import edits,mod,trend
from products.models import products

def home(request):
    gamesitedata=edits.objects.all().order_by('-id')
    gameedata=mod.objects.all().order_by('-id')
    trenddata=trend.objects.all()
    productsdata=products.objects.all()
    paginator=Paginator(productsdata,4)
    page_number=request.GET.get('page')
    productsdatafinal=paginator.get_page(page_number)

    data={
        'gamesitedata':gamesitedata,
        'gameedata':gameedata,
        'trenddata':trenddata,
        'productsdata':productsdata,
        'productsdata':productsdatafinal,
    } 
    return render(request,"home.html",data)