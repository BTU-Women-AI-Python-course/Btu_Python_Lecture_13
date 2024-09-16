from django.urls import path

from product.views import contact_view, product_form

urlpatterns = [
    path('contact/', contact_view, name='contact_view'),
    path('product_form/', product_form, name='product_form'),
]
