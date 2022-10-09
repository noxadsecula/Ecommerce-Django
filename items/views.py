from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
def index(request):
    items = Item.objects.all()
    category = Category.objects.all()

    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        items = Item.objects.filter(
            Q(name__icontains = search) |
            Q(cat__iName__icontains = search)
        )

    context = {
        'items' : items,
        'category': category,
        'search': search
    }


    return render(request, 'index.html',context)

def shop(request):
    return render(request, "shop.html")

def contact(request):
    return render(request, 'contact.html')