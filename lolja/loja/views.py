from tkinter import Entry
from django.shortcuts import render
from loja.models import Site, Carousel
from django.http import HttpResponse

# Create your views here.

def index(request):
    all_products = Site.objects.all() 
    all_carousel = Carousel.objects.all()
    return render(request, "index.html", {"guitarras": all_products, "carousel": all_carousel})
    
def cart(request):
    return render(request, 'carrinho.html')

def price(request):
    return render(request, 'produtos.html')

def test1(request):
    #all_entries = Site.objects.get(id=1)
    #resulta = []
    #for x in all_entries:
    #    formatador = "x.nome.card+"
    #    resulta.append()
    retornar = all_entries.nome_card + " | " + all_entries.description + " | "

    return HttpResponse(retornar)