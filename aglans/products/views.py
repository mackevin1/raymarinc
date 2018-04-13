from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'products/index.html',{})
def index(request):
     return render(request, 'index.html', {})
