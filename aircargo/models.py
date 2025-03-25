from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    FREIGHT_CHOICES = [
        ('air', 'Air Freight'),
        ('sea', 'Sea Freight'),
        ('road', 'Road Freight'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    freight = models.CharField(max_length=10, choices=FREIGHT_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    date_posted = models.DateField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.full_name