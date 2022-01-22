from django.utils.safestring import mark_safe
from django.db import models


# Create your models here.
class Category(models.Model):
    status = {
        ('True','True'),
        ('False','False'),
    }


    title =models.CharField(max_length=200)
    Image =models.ImageField(blank=True,upload_to='category/')
    status =models.CharField(max_length=20,choices=status)
    slug =models.CharField(max_length=150, null=False, blank=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def ImageUrl(self):
        if self.Image:
            return self.Image.url
        else:
            return ""


class Product(models.Model):
    status = {
        ('True','True'),
        ('False','False'), }

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='product/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    detail = models.TextField()
    status = models.CharField(max_length=20, choices=status)
    slug =models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'
    

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""