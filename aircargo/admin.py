from django.contrib import admin
from .models import ContactMessage
from .models import News
from .models import Contact
from .models import Cargo
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from django.db import models


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

    # Apply CKEditorWidget to the RichTextField
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()},  # Correct import here
    }

admin.site.register(News, NewsAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name', 'email')

class CargoAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'carrier_name', 'status', 'transport_mode', 'departure_location', 'destination_location', 'estimated_delivery')
    list_filter = ('status', 'transport_mode')  # Add transport mode to filters
    search_fields = ('tracking_number', 'carrier_name', 'departure_location', 'destination_location')

admin.site.register(Cargo, CargoAdmin)