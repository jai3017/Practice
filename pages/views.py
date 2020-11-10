from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices,bedroom_choices,state_choice


from listings.models import listing
from realtors.models import Realtors

def index(request):
    listings=listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'state_choice':state_choice,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
    }
    return render(request,'pages/index.html',context)

def about(request):

    realtors=Realtors.objects.order_by('-hire_date')

    mvp_realtors=Realtors.objects.all().filter(is_mvp=True)
    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors,
    }
    return render(request,'pages/about.html',context)