from django.urls import path
from . import views
from django.conf import settings
from .views import home_view, contact_view
from django.conf.urls.static import static
from .views import tracking_result
from .views import news_list, news_detail

urlpatterns = [
    path('', home_view, name='home'),  
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', contact_view, name='contact'),
    path('tracking-result/', tracking_result, name='tracking_result'),  # Add this new route
    path('news/', news_list, name='news_list'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('blog/', views.blog, name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)