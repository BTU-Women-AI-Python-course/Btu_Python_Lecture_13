from django.shortcuts import render
from product.forms import ContactForm, ProductForm


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
            return render(request, 'success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # Redirect to a success page
    else:
        form = ProductForm()

    return render(request, 'product_form.html', {'form': form})
