from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.hashers import make_password
class RegisterUser(models.Model):
   Firstname = models.CharField(max_length=100)
   Lastname= models.CharField(max_length=100)
   regemail = models.EmailField(unique=True)
   regpassword = models.CharField(max_length=100)
   def __str__(self):
      return f"{self.Firstname} {self.Lastname} {self.regemail} {self.regpassword}"

class RegisterCategory(models.Model):
   category_name = models.CharField(max_length=100)
   category_description = models.CharField(max_length=255)
   def __str__(self):
      return f"{self.category_name} {self.category_description}"
class RegisterBrand(models.Model):
   brand_name = models.CharField(max_length=100)
   def __str__(self):
      return f"{self.brand_name}"

class Addproduct(models.Model):
   product_name = models.CharField(max_length=100)
   serial_number = models.CharField(max_length=100, unique=True)
   product_category = ForeignKey(RegisterCategory, on_delete=models.CASCADE)
   product_brand = ForeignKey(RegisterBrand, on_delete=models.CASCADE)
   product_Bprice = models.DecimalField(max_digits=10, decimal_places=2)
   product_Sprice = models.DecimalField(max_digits=10, decimal_places=2)
   product_image = models.ImageField()

   