# Initial Set Up

## File System Layout

```php
hknbe-website
├── .gitignore
├── README.md
├── creation.md
├── hknbe_website
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── settings.cpython-310.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── base.html
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt
├── static
│   └── css
│       ├── output.css
│       └── styles.css
└── tailwind.config.js
```

## Step 1: Setting Up The Django Project

### 1. Create a Virtual Environment

This environment was named such since I was using Python 3.10 at the time. This allows me to make other environments to upgrade python versions.

```shell
mkdir hknbe_website
cd hknbe_website
python -m venv .venv310
source .venv310/bin/activate
```

### 2. Install Django

```shell
pip install django
```

### 3. Start a New Django Project

Create the Django project and then pull everything out of the outermost folder created for convenience.

```shell
django-admin startproject hkn_website
mkdir tmp
mv hknbe_website/* tmp
rmdir hknbe_website
mv tmp/* .
rmdir tmp
```

### 4. Create a Django App

The `main` Django app will house the homepage and all the info pages.

```shell
python manage.py startapp main
```

### 5. Register the App in `settings.py`

Add `main` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...,
    'main',
]
```

### 6. Adjust `SECRET_KEY` in `settings.py`

Move the secret key from `settings.py` into a new file called `secret.py`. Then change `settings.py` to import the key from `secret.py` so it is protected. This way the secret key won't accidentally get put into the github repo.


## Step 2: Install and Configure Tailwind CSS

### 1. Install Tailwind CSS via npm

Had some permission issues so I had to use `sudo` for the installation part.

```shell
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```

### 2. Configure Tailwind Content Paths

Update `tailwind.config.js` to include your Django templates and static files:

```js
module.exports = {
  content: [
    './templates/**/*.html',  // Django templates
    './static/**/*.js',       // JavaScript files
  ],
  theme: {
    extend: {
      colors: {
        primary: '#007BFF',  // IEEE-HKN blue
        secondary: '#6C757D', // Gray
      },
    },
  },
  plugins: [],
};
```

### 3. Add Tailwind Directives to Your CSS

Create a custom CSS file, e.g., `static/css/styles.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Custom styles */
body {
  font-family: 'Inter', sans-serif;
}
```

### 4. Build the Tailwind CSS

Run the following command to generate the `output.css` file:

```shell
npx tailwindcss -i ./static/css/styles.css -o ./static/css/output.css --watch
```


## Step 3: Configure Django to Serve Static Files

### 1. Update `settings.py` for Static Files

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

### 2. Include the Tailwind CSS in Your Templates

Create `main/templates/`. In `templates/base.html`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IEEE-HKN Website</title>
    <link href="{% static 'css/output.css' %}" rel="stylesheet">
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```


## Step 4: Build Your Django Views and Templates

### 1. Create URLs

Create `main/urls.py`. In `main/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about_page, name='about_page'),
]
```

In `hkn_website/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

### 2. Create Views

In `main/views.py`:

```python
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')

def about_page(request):
    return render(request, 'about.html')
```

### 3. Create Templates

Create `templates/landing.html`:

```html
{% extends 'base.html' %}
{% block content %}
<h1 class="text-primary text-4xl font-bold">Welcome to IEEE-HKN</h1>
<p class="text-secondary">This is the landing page.</p>
{% endblock %}
```

Create `templates/about.html`:

```html
{% extends 'base.html' %}
{% block content %}
<h1 class="text-primary text-4xl font-bold">About IEEE-HKN</h1>
<p class="text-secondary">Learn more about us!</p>
{% endblock %}
```


## Step 5: Run the Development Server

### 1. Apply Migrations

```shell
python manage.py migrate
```

### 2. Start the Server

```shell
python manage.py runserver
```

Go to http://127.0.0.1:8000/ to see the website.