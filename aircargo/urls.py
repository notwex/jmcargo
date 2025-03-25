from django.urls import path
from . import views
from django.conf import settings
from .views import home_view, contact_view
from django.conf.urls.static import static

urlpatterns = [
   
    path('', home_view, name='home'),  
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', contact_view, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)