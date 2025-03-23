from django.contrib import admin
from .models import ContactMessage
from .models import News

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'freight', 'submitted_at')
    list_filter = ('freight', 'submitted_at')
    search_fields = ('name', 'email', 'mobile')

admin.site.register(ContactMessage, ContactMessageAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    search_fields = ('title',)
    list_filter = ('date_posted',)

admin.site.register(News, NewsAdmin)
