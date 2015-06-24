from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField("person's first name", max_length=30)
    last_name = models.CharField("person's last name", max_length=30)

    SHIRT_SIZES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    )
    # within choices
    shirt_size = models.CharField(choices=SHIRT_SIZES, max_length=1, default="S")
    # p.shirt_size #M
    # p.get_shirt_size_display() #Medium
