from django import forms
from django.core.exceptions import ValidationError

from products.models import Product


def validate_name(value):
    if value.isnumeric():
        raise ValidationError(
            "%(value)s is numeric.",
            params={"value": value},
        )


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=255, validators=[validate_name])

    class Meta:
        model = Product
        fields = ["name", "description", "price", "category"]
