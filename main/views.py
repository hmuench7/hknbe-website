from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')

def about_page(request):
    return render(request, 'about.html')
