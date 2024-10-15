from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    profile=models.ImageField(default="pp1.PNG",null=True,blank=True)
    phone=models.CharField(max_length=20, null=True)
    email=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.name)
class Book(models.Model):
    CATEGORY=(
        ('fiction','fiction'),
        ('religious','religious'),
        ('Programming/Web Development','Programming/Web Development'),
        ('Self-Help','Self-Help'),   
    )
    title=models.CharField(max_length=200, null=True)
    author=models.CharField(max_length=200, null=True)
    price= models.FloatField(null=True)
    category=models.CharField(max_length=5000, null=True, choices=CATEGORY)
    description=models.TextField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title
class Order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('delivered','delivered'),
    )
    customer=models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    book=models.ForeignKey(Book,null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True, choices=STATUS,default="pending")
    note=models.CharField(max_length=2000, null=True)
    def __str__(self):
        return str(self.status)