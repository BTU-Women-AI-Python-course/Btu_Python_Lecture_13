from django.urls import path

from products.views import create_product

urlpatterns = [
    path("create/", create_product, name="products-create")
]
