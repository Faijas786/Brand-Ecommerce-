from django.db import models

# Create your models here.


class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discountprice=models.IntegerField()
    description=models.TextField()
    rating=models.FloatField()
    category=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.title    

class Discount(models.Model):
    title=models.CharField(max_length=200)
    discounts=models.IntegerField()
    image=models.ImageField(upload_to='media/')
    def __str__(self):
        return self.title 
    
class Banner(models.Model):
   title=models.CharField(max_length=200)
   description=models.TextField()
   image=models.ImageField(upload_to='media/')
   def __str__(self):
        return self.title 
   
class Sidebanner(models.Model):
   title=models.CharField(max_length=200)
   image=models.ImageField(upload_to='media/')
   def __str__(self):
        return self.title 

class Services(models.Model):
   title=models.CharField(max_length=200)
   image=models.ImageField(upload_to='media/')
   def __str__(self):
        return self.title 
 
  