from django.shortcuts import render
from .models import listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.shortcuts import get_object_or_404
from .choices import price_choices,bedroom_choices,state_choice

def index(request):
    listings=listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,2)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings':paged_listings
    }

    return render(request,'listings/listings.html',context)

def listings(request,listing_id):
    listings=get_object_or_404(listing,pk=listing_id)
    context={
        'listing':listings
    }
    return render(request,'listings/listing.html',context)

def search(request):
    queryset_list=listing.objects.order_by('-list_date')
    # search with description
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)

    # search using city

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)

    # price
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)


    context = {
        'listings': listings,
        'state_choice': state_choice,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listing':queryset_list,
        'values':request.GET,
    }
    return render(request,'listings/search.html',context)