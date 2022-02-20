from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Product(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model_in':('book','cupboard',)})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type','object_id')

    class Meta:
        ordering = ['object_id']

class Base(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created',)

class Book(Base):
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

class Cupboard(Base):
    shelves = models.IntegerField()
    author = models.CharField(max_length=255)