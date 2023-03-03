from django.contrib import admin
from .models import Sell

# Register your models here.
class SellAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Sell, SellAdmin)