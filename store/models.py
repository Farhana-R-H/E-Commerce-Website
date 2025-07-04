from django.db import models

CATEGORY_CHOICES = [
    ('relax', 'Relax & Refresh'),
    ('eco', 'Eco-Friendly Care'),
     ('hair', 'Herbal Hair Care'),
    ('powders', 'Natural Powders & Scrubs'),
    ('kits', 'Self-Care Kits'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    image_main = models.ImageField(upload_to='products/')
    image_2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.FloatField()
    description = models.TextField()
    rating = models.FloatField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    purchases = models.IntegerField(default=0)  # 👈 Add this field
    ingredients = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, help_text="List product highlights like 'Biodegradable, Compostable, Reusable'")
    skin_type = models.CharField(max_length=100, blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
