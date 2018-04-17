from django.shortcuts import render
from .models import Board
from products.models import product_views

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
def post_list(request):
    context = {
            'products': Products.objects.all(),
            'boards': Boards.objects.all(),
        }
    return render(request, 'products/index.html',{})
