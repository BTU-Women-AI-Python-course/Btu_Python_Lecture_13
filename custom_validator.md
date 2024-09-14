# Django Custom Validator Example

This example demonstrates how to create and use a custom validator in Django to ensure that a field contains an even number.

### Custom Validator

First, define the custom validator `validate_even` in your validators file (e.g., `validators.py`):

```python
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value},
        )
```

### Using the Validator in a Django Model

You can use the `validate_even` function in a Django model by including it in the `validators` argument for a field:

```python
from django.db import models
from .validators import validate_even  # Import the custom validator

class MyModel(models.Model):
    even_number = models.IntegerField(validators=[validate_even])
```

In this model, the `even_number` field will only accept even numbers. If an odd number is provided, a `ValidationError` will be raised.

### Using the Validator in a Django Form

To use the `validate_even` validator in a Django form:

```python
from django import forms
from .validators import validate_even  # Import the custom validator

class MyForm(forms.Form):
    even_number = forms.IntegerField(validators=[validate_even])
```

This form will validate the `even_number` field to ensure it contains an even number before processing the data.
