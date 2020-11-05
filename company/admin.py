from django.contrib import admin
from .models import CompanyProfile

class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'email', 'about', 'logo']

admin.site.register(CompanyProfile, CompanyProfileAdmin)
