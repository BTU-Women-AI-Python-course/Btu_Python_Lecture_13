from django import forms

from product.models import Product
from product.validators import validate_age


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
    age = forms.IntegerField(label='Age', validators=[validate_age])


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'active', 'categories', 'tags']
