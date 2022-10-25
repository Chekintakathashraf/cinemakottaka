
from email.policy import default
from django.db import models
from django.urls import reverse

# Create your models here.

class District(models.Model):
    district = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.district

class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.city

class Cityenquery(models.Model):
    cityenqueryname = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=255)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.cityenqueryname

class Category(models.Model):
    
    category_name = models.CharField(max_length = 50,unique = True)
    slug          = models.SlugField(max_length = 100, unique = True)

    class Meta:
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('movie_by_category', args = [self.slug])

    def __str__(self):
        return self.category_name

class Movie(models.Model):

    tmdb_id = models.CharField(max_length=20,null=True,blank=True)
    movie_name = models.CharField(max_length=50,null=True,blank=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    # name = models.CharField(max_length=50,null=True,blank=True)
    

    is_active  = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.movie_name