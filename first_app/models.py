from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ActiveProductsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField('ProductTag', blank=True, related_name='tags')
    one_to_one = models.OneToOneField(
        'SomeEntity',
        on_delete=models.SET_NULL,
        null=True,
        related_name='one_to_one',
    )

    objects = models.Manager()
    active_objects = ActiveProductsManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('first_app:product_detail', kwargs={'product_slug': self.slug})


class SomeEntity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class ProductTag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.title
