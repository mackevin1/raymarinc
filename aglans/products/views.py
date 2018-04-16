from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def post_list(request):
    return render(request, 'products/index.html',{})
def index(request):
        boards = products.objects.all()
     return render(request, 'index.html', {'boards': boards})
