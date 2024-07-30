from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'stockout/index.html')

def add_stockout(request):
    return render(request, 'stockout/add_stockout.html')

