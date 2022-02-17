
from django.conf import settings
from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone




class Category(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=200)


# search products and filter products on the basis of categories and also filter project on the basis of date range
class Product(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    content = models.CharField(max_length=500,null=True)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title


