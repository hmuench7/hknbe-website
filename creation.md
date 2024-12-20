# Initial Set Up

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

