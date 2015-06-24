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


class Group(models.Model):
    name = models.CharField(max_length=13)
    members = models.ManyToManyField(Person, through="Membership")


class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateTimeField()
    invite_reason = models.CharField(max_length=64)


class Manufacturer(models.Model):
    pass


class Cars(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)


class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"


class Topping(models.Model):
    pass


class Pizza(models.Model):
    # It doesn¡¯t matter which model has the ManyToManyField, but you should only put it in one of the models ¨C not both.
    toppings = models.ManyToManyField(Topping)
