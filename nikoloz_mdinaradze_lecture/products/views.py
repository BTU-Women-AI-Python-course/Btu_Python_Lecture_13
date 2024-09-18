from django.http import HttpResponse
from django.shortcuts import render

from products.forms import ProductForm


# Create your views here.
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Product created !!!")
    else:
        form = ProductForm()
    return render(request, "products/products_create.html", {"form": form})

