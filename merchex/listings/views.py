from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def hello(request):
    #mettre à jour la vue pour afficher objet de groupe
    bands = Band.objects.all()

    return render(request, "listings/hello.html",
                  {"bands": bands})

def about(request):
    return render(request,"listings/about.html")

def listings(request):
    listing = Listing.objects.all()

    return render(request, "listings/listing.html",
                  {"listing": listing})

def contact(request):
    return render(request,"listings/contact.html")