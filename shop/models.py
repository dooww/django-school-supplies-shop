from django.db import models
from company.models import CompanyProfile

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='products')
    price = models.IntegerField()
    description = models.TextField()
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    publishing_end_date = models.DateTimeField()
    schooltype_choice = (
        ('praktijkonderwijs','praktijkonderwijs'),
        ('vmbo','vmbo'),
        ('mbo','mbo'),
        ('hbo','hbo'), 
        ('opleidingsbedrijf','opleidingsbedrijf')
    )
    schooltype = models.CharField(choices=schooltype_choice, max_length=6)
    category_choice = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )
    category = models.CharField(choices=category_choice, max_length=6)

    def __str__(self):
        return self.name
