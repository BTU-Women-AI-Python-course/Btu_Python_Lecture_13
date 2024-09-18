from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product


# Create your views here.
def create_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            category=request.POST['category']
        )
        return HttpResponse("Product created !!!")
    return render(request, "products/products_create.html")

