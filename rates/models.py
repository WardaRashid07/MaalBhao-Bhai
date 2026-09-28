from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Material(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('sqft', 'Square foot'),
        ('m', 'Meter'),
        ('dozen', 'Dozen'),
        ('piece', 'Piece'),
    ]
    name = models.CharField(max_length=150)
    urdu_name = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='materials')
    grade = models.CharField(max_length=150, blank=True)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PriceQuote(models.Model):
    SOURCE_TYPES = [
        ('quote', 'Supplier quote'),
        ('indicative', 'Indicative'),
        ('benchmark', 'Market benchmark'),
    ]
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='quotes')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    source_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES)
    quote_date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.material.name} — Rs {self.price} ({self.source_name})"

    class Meta:
        ordering = ['-quote_date']