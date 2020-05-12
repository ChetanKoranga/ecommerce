from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length = 50)
    category_name = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    subcategory_name = models.ManyToManyField(SubCategory, blank=True)
    category_name = models.ManyToManyField(Category, blank=True)
    
    def __str__(self):
        return self.product_name



    def __str__(self):
        return self.subcategory_name

    def __str__(self):
        return self.category_name