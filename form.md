# Django Form

### Example: Contact Form

## **Create a Form**

First, define your form in a file named `forms.py` within your Django app directory.

```python
# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
```

## **Create a View**

Next, create a view to handle the form in `views.py`.

```python
# views.py
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # For demonstration, we'll just print the data
            print(f"Name: {name}, Email: {email}, Message: {message}")
            # Redirect or show a success message here
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

## **Create a Template**

Create a template `contact.html` in your templates directory to render the form.

```html
<!-- contact.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Send</button>
    </form>
</body>
</html>
```

In Django templates, `form.as_p` is a method provided by Django's form handling system that renders a form as HTML `<p>` tags for each form field.

Here's a breakdown:

- **`form`**: An instance of a Django form class.
- **`as_p`**: A method of the form instance that returns a string of HTML where each form field is wrapped in `<p>` tags.
  
**csrf token**

The `{% csrf_token %}` tag is used in Django templates to include a CSRF (Cross-Site Request Forgery) token in the form. This token is a security measure that helps protect your website from CSRF attacks.

When a user submits a form, the CSRF token included in the form is sent back to the server. Django then checks this token to ensure that the form submission is coming from a trusted source, not from a potentially malicious site. If the token is missing or incorrect, Django will reject the form submission, thereby preventing unauthorized actions.

**What `as_p` Does**

When you use `{{ form.as_p }}` in a template, Django generates HTML like this:

```html
<form method="post">
    <p>
        <label for="id_name">Your Name:</label>
        <input type="text" name="name" maxlength="100" id="id_name">
    </p>
    <p>
        <label for="id_email">Your Email:</label>
        <input type="email" name="email" id="id_email">
    </p>
    <p>
        <label for="id_message">Message:</label>
        <textarea name="message" id="id_message"></textarea>
    </p>
    <!-- CSRF token and submit button would be here -->
</form>
```

**Other Methods**

Django forms also provide other methods to render forms:

- **`form.as_table`**: Renders the form fields as HTML table rows (`<tr>`).
- **`form.as_ul`**: Renders the form fields as list items (`<li>`).

Each of these methods allows for different HTML structures, making it easy to format forms according to your design needs.

## **Add a URL Pattern**

Add a URL pattern to `urls.py` to route requests to your view.

```python
# urls.py
from django.urls import path
from .views import contact_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
]
```

### Explanation

- **`forms.py`**: Defines a simple form with fields for name, email, and message.
- **`views.py`**: Contains a view that handles both GET and POST requests. On GET requests, it displays an empty form. On POST requests, it processes the form data if the form is valid.
- **`contact.html`**: Renders the form and includes the CSRF token for security.
- **`urls.py`**: Maps the URL `/contact/` to the `contact_view`.

