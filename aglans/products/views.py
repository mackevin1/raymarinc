from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def post_list(request):
    return render(request, 'products/index.html',{})
def index(request):
     return render(request, 'index.html', {})

def index(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
