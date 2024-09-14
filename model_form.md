# Django Model Form

### Example: User Profile Model Form

1. **Define a Model**

First, define a model in `models.py`.

```python
# models.py
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
```

2. **Create a ModelForm**

Next, create a form for the model in `forms.py`.

```python
# forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birth_date']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
```

3. **Create a View**

Create a view to handle the form in `views.py`.

```python
# views.py
from django.shortcuts import render, redirect
from .forms import UserProfileForm

def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_success')  # Redirect to a success page
    else:
        form = UserProfileForm(instance=request.user.profile)

    return render(request, 'user_profile.html', {'form': form})
```

4. **Create a Template**

Create a template `user_profile.html` to render the form.

```html
<!-- user_profile.html -->
<!DOCTYPE html>
<html>
<head>
    <title>User Profile</title>
</head>
<body>
    <h1>Edit Profile</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
```

**csrf token**

The `{% csrf_token %}` tag is used in Django templates to include a CSRF (Cross-Site Request Forgery) token in the form. This token is a security measure that helps protect your website from CSRF attacks.

When a user submits a form, the CSRF token included in the form is sent back to the server. Django then checks this token to ensure that the form submission is coming from a trusted source, not from a potentially malicious site. If the token is missing or incorrect, Django will reject the form submission, thereby preventing unauthorized actions.


5. **Add a URL Pattern**

Add a URL pattern to `urls.py` to route requests to your view.

```python
# urls.py
from django.urls import path
from .views import user_profile_view

urlpatterns = [
    path('profile/', user_profile_view, name='user_profile'),
    path('profile/success/', TemplateView.as_view(template_name='profile_success.html'), name='profile_success'),
]
```

### Explanation

- **`models.py`**: Defines a `UserProfile` model with fields for `bio` and `birth_date`.
- **`forms.py`**: Creates a `UserProfileForm` ModelForm that includes `bio` and `birth_date` fields. The `widgets` attribute customizes the appearance of these fields.
- **`views.py`**: Defines a view to handle form submission. It pre-fills the form with existing profile data when rendered with a GET request, and saves the form data when submitted with a POST request.
- **`user_profile.html`**: Renders the form using `{{ form.as_p }}` to display each field in a paragraph.
- **`urls.py`**: Maps the `/profile/` URL to the `user_profile_view` and includes a success URL for redirection after successful form submission.

This example shows how to create a form tied to a model, customize its appearance, and handle form submission in Django.
