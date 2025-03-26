from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ContactMessage
from .models import News
from .models import Contact
from django.contrib import messages
from .models import Cargo

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        freight = request.POST.get('freight')
        message = request.POST.get('message')

        # Save form data to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            freight=freight,
            message=message
        )

        messages.success(request, "Your message has been submitted successfully!")
        return redirect('home')  # Change 'home' to your actual home URL name

    return render(request, 'home.html')


def home_view(request):
    latest_news = News.objects.order_by('-date_posted')[:10]  # Get the 10 latest news posts
    return render(request, 'home.html', {'latest_news': latest_news})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def contact_view(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        contact = Contact(full_name=full_name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'contact.html')

def tracking_result(request):
    tracking_number = request.GET.get('tracking_number', None)
    if tracking_number:
        try:
            cargo = Cargo.objects.get(tracking_number=tracking_number)
            return render(request, 'tracking_result.html', {'cargo': cargo})
        except Cargo.DoesNotExist:
            messages.success(request, 'Tracking number not found.')
            return render(request, 'home.html')
    return render(request, 'home.html', {'error': 'Please enter a tracking number.'})

def news_list(request):
    latest_news = News.objects.all().order_by('-date_posted')[:5]  # Get latest 5 news
    return render(request, 'home.html', {'latest_news': latest_news})

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    more_news = News.objects.exclude(id=news_id).order_by('-date_posted')[:5]  # Get more news
    return render(request, 'news_detail.html', {'news': news, 'more_news': more_news})

def blog(request):
    latest_news = News.objects.order_by('-date_posted')[:10]  # Get the 10 latest news posts
    return render(request, 'blog.html', {'latest_news': latest_news})