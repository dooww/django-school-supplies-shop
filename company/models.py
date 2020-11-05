from django.db import models
#from django.contrib.auth.models import User

class CompanyProfile(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    about = models.TextField(null=True)
    logo = models.ImageField(upload_to='company')
    website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
