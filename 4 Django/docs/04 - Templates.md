# Templates

- [Templates](#templates)
  - [Passing a Value to the Template](#passing-a-value-to-the-template)
  - [Template Rendering Syntax](#template-rendering-syntax)
    - [Rendering a Value](#rendering-a-value)
    - [Conditionals](#conditionals)
    - [Looping](#looping)
  - [Reverse URL Lookup](#reverse-url-lookup)
  - [Forms](#forms)
  - [Static Files](#static-files)
  - [Template Inheritance](#template-inheritance)
      - [base.html](#basehtml)
      - [index.html](#indexhtml)
      - [detail.html](#detailhtml)

Templates are like blueprints for your HTML pages. They contain plain HTML/CSS/JavaScript, but also additional syntax for generating HTML/CSS/JavaScript using variables from your Python view. You can read more about Templates [here](https://docs.djangoproject.com/en/3.0/topics/templates/) and [here](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)

The variable names referred to inside the template must be defined in the data context (a dictionary) passed to the `render` function inside the view. For more information, see the [views doc](02%20-%20Views.md).

## Passing a Value to the Template


## Template Rendering Syntax

### Rendering a Value

You can render a value in a template using `{{}}`.


**views.py**
```python
from django.shortcuts import render
def index(self)
    return render(request, 'myapp/index.html', {'name': 'Jane'})
```
**index.html**
```html
<span>Hello, {{name}}!</span>
```

### Conditionals

What you put inside an `if` block will only be rendered if the condition is true.

**views.py**
```python
from django.shortcuts import render
def index(self)
    return render(request, 'myapp/index.html', {'temperature': random.randint(50, 100)})
```
**index.html**
```html
{% if temperature < 60 %}
<span>cold</span>
{% elif temperature < 80 %}
<span>warm</span>
{% else %}
<span>hot</span>
{% endif %}
```

### Looping

Whatever you put inside the `for` block will be repeated for each iteration of the loop. For example, we can build a list of items.

**views.py**
```python
from django.shortcuts import render
def index(self)
    return render(request, 'myapp/index.html', {'fruits': ['apples', 'bananas', 'pears']})
```
**index.html**
```html
<ul>
    {% for fruit in fruits %}
    <li>{{ fruit }}</li>
    {% endfor %}
</ul>
```


## Reverse URL Lookup

In order for Django to find the proper path when rendering the template, the app's `urls.py` must contain the variable `app_name`, e.g. `app_name = 'todos'`.


**urls.py**
```python
from django.urls import path
from . import views
app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add')
]
```

**index.html**
```html
<form action="{% url 'todos:add' %}" method="post">
    {% csrf_token %}
    <input type="text" name="todo_text"/>
    <button type="submit">+</button>
</form>
```


The `name` given in `urls.py` and the actual `path` can be different. To keep things simple, use consistent names. You can read more about [routing](https://docs.djangoproject.com/en/3.0/topics/http/urls/) and the [urls package](https://docs.djangoproject.com/en/3.0/ref/urls/).


## Forms

A form is an HTML element that can transmit data to a server. Forms have two important attributes: `action` and `method`. The `action` is the url to which the form's data will be submitted. The `method` is the HTTP method (POST, GET, PUT, DELETE).

The `input` elements inside a form. To 'submit' the data, add a button with `type="submit` inside the form. You can read more about forms [here](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Your_first_HTML_form).

Django also requires a CSRF token to be submitted as part of the form. CSRF stands for 'cross-site request forgery' You can include this just by adding `{% csrf_token %}` inside the form. You can read more about CSRF [here](https://en.wikipedia.org/wiki/Cross-site_request_forgery).

```html
<form action="/savetodo" method="post">
    {% csrf_token %}
    <input type="text" name="todo_text"/>
    <button type="submit">+</button>
</form>
```

## Static Files

To load static files into a page, create a folder in your app called `static`. Inside that folder, create a folder with the same name as your app (just as you did with templates). In your template, you then must add `{% load static %}` before you load your static file.

- [Managing Static Files](https://docs.djangoproject.com/en/3.0/howto/static-files/)
- [Polls Tutorial: Part 6](https://docs.djangoproject.com/en/3.0/intro/tutorial06/)

```html
{% load static %}
<img src="{% static 'todos/example.jpg' %}" alt="My image"/>
```

## Template Inheritance

You can have one template 'inherit' from another, meaning the child template's content will be included inside the parent. You can accomplish this by putting a `{% block content %} / {% endblock %}` in the parent and an `{% extends '<app name>/<parent>.html' %}` in the child. This is useful if your header/footer/menus are consistent across multiple pages and you don't want to repeat the HTML. You can read more about template inheritance [here](https://tutorial.djangogirls.org/en/template_extending/).

In the example below, `base.html` contains the header and footer and a global CSS file. Two pages, `index.html` and `detail.html` inherit from `base.html`. Each page's title and content is then substituted for the block in `base.html` when the template is rendered.


#### base.html

```html
{% load static %}
<head>
    <link rel="stylesheet" type="text/css" href="{% static 'myapp/style.css' %}"/>
</head>
<body>
    <h1>{% block title %}{% endblock %}</h1>
    <hr/>
    {% block content %}
    {% endblock %}
    <hr/>
    (c) myapp inc
</body>
```

#### index.html

```html
{% extends 'myapp/base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
<p>this is the page content for the index page</p>
{% endblock %}
```

#### detail.html

````html
{% extends 'myapp/base.html' %}

{% block title %}Details{% endblock %}

{% block content %}
<p>this is content for the detail page</p>
{% endblock %}
````
