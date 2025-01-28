from django.shortcuts import render
from .models import Announcement, LeadershipMember, LeadershipPosition

def home(request):
    announcements = Announcement.objects.order_by('-created_at')[:5]
    return render(request, 'home.html', {'announcements': announcements})


def landing_page(request):
    return render(request, 'landing.html')

def about_page(request):
    return render(request, 'about.html')

def why_join_hkn(request):
    return render(request, 'why_join_hkn.html')

def leadership(request):
    positions = LeadershipPosition.objects.prefetch_related('leaders').all()
    return render(request, 'leadership.html', {'positions': positions})

def tutoring(request):
    return render(request, 'tutoring.html')

def db_cafe(request):
    return render(request, 'db_cafe.html')
