# goldpresentprice/models.py

from django.db import models

class GoldPrice(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define the primary key type
    # Other fields...


    def __str__(self):
        return f"Gold Price on {self.date}: ${self.price}"
