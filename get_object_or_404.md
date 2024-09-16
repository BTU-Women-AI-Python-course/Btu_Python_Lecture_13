# Get object in django

`get_object_or_404` is a shortcut function in Django that retrieves an object from the database or 
raises a `Http404` exception if the object does not exist. It's a convenient way to handle the scenario where 
a requested object might not be present, ensuring that your view does not 
crash or return an error when a user accesses a non-existent object.

### Example Usage

Let's say you have a model called `Article` and you want to get a specific article by its primary key (`pk`). You can use `get_object_or_404` in your view as follows:

```python
from django.shortcuts import get_object_or_404
from .models import Article

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})
```

### Explanation

- **`get_object_or_404(Article, pk=pk)`**: This line attempts to retrieve an `Article` object from the database where the primary key matches the given `pk`. 
- **If the object is found**: It returns the `Article` object and assigns it to the variable `article`.
- **If the object is not found**: It raises an `Http404` exception, which is then handled by Django to show a "Page not found" error to the user.
- **Benefits**: Using `get_object_or_404` makes your code cleaner and more concise by avoiding the need to manually handle the case where the object does not exist.

### How It Works

Internally, `get_object_or_404` uses the model's `get()` method to fetch the object. If `get()` raises a `DoesNotExist` exception, `get_object_or_404` catches this exception and raises an `Http404` exception instead.

### Alternative Without `get_object_or_404`

Here's how you might write the same view without using `get_object_or_404`:

```python
from django.http import Http404
from .models import Article

def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'article_detail.html', {'article': article})
```

Using `get_object_or_404` is preferred as it simplifies this logic into a single line and improves code readability.
