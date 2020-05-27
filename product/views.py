from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):
    product_list = Product.objects.all()
    context = {'products': product_list}
    return render(request, 'product/index.html',context)
