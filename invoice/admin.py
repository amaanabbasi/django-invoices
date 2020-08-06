from django.contrib import admin

from .models import Invoice, LineItem

admin.site.register(Invoice)
admin.site.register(LineItem)
# Register your models here.
