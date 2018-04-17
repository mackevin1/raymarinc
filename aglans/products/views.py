from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from .models import Boards

# Create your views here.
def post_list(request):
    context = {
            'products': Products.objects.all(),
            'boards': Boards.objects.all(),
        }
            return render(request, 'products/index.html',{})
def index(request):
    boards = Products.objects.all()
    return render(request, 'index.html', {'boards': boards})
def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
