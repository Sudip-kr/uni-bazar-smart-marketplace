from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    CATEGORY_CHOICES = (
        ('books', 'Books'),
        ('electronics', 'Electronics'),
        ('cycles', 'Cycles'),
        ('kitchen', 'Kitchen Appliances'),
        ('hostel_essentials', 'Hostel Essentials'),
        ('furniture', 'Furniture'),
        ('other', 'Other'),
    )

    CONDITION_CHOICES = (
        ('new', 'Like New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('used', 'Used'),
    )

    LOCATION_TYPE_CHOICES = (
        ('hostel', 'Hostel'),
        ('day_scholar', 'Day Scholar'),
    )

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sold', 'Sold'),
    )

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='good')
    location_type = models.CharField(max_length=20, choices=LOCATION_TYPE_CHOICES)
    hostel_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    wishlist = models.ManyToManyField(User, related_name='wishlist_items', blank=True)

    def __str__(self):
        return self.title