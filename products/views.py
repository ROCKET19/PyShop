from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Forum


def index(request):
    pdt = Product.objects.all()
    return render(request, 'forum.html', {'pdt': pdt})

# def new(request):
# forum = Forum.objects.all()
# return render(request, 'index.html', {'forum': forum})
# return HttpResponse()
