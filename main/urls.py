from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing Page
    path('about/', views.about_page, name='about_page'),  # About Page
    path('about/why-join-hkn/', views.why_join_hkn, name='why_join_hkn'),  # Why Join HKN
    path('about/leadership/', views.leadership, name='leadership'),  # Leadership
    path('about/tutoring/', views.tutoring, name='tutoring'),  # Tutoring
    path('about/db-cafe/', views.db_cafe, name='db_cafe'),  # dB Cafe
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
