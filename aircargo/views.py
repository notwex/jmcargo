from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from .models import News

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
    latest_news = News.objects.order_by('-date_posted')[:3]  # Get the 3 latest news posts
    return render(request, 'home.html', {'latest_news': latest_news})

def about(request):
    return render(request, 'about.html')