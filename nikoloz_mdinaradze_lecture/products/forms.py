from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    price = forms.FloatField()
    category = forms.CharField(max_length=255)
