from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=30)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=10)
    detail = models.TextField(max_length=1000)
    featured = models.BooleanField()
    slug = models.SlugField(default="", null=False)
    category_id = models.ForeignKey('category',on_delete=models.CASCADE , related_name='product')
    image = models.ImageField(upload_to='static/img/product-img/',default='static/img/product-img/product-1.jpg')
    def __str__(self):
        return(self.name)

from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(product, blank=True)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True) 



class category(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return(self.name)

# class cart(models.Model):
#     user_id = models.ForeignKey(User,on_delete=models.CASCADE , related_name='cart')
#     product_id = models.ForeignKey('product',on_delete=models.CASCADE , related_name='cart')

class Review(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/product-img/')
    description = models.TextField()
    rating = models.IntegerField()
    def __str__(self):
        return(self.description)
