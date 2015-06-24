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

    def _get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    full_name = property(_get_full_name)

    def get_absolute_url(self):
        pass


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


class Car(models.Model):
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


"""Overriding Examples"""


class Blog(models.Model):
    name = models.CharField(max_length=20)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        # You can prevent saving
        if self.name == "Jordan's Blog":
            return  # Jordan shall never have his blog!

        # do_something()
        super(Blog, self).save(*args, **kwargs)
        # do_something_else()

        # you can use pre_delete and/or post_delete signals.
        # Unfortunately, there isn¡¯t a workaround when creating or updating objects in bulk, since none of save(), pre_save, and post_save are called.


"""Abstract Model"""


class CommonModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ["name"]


class Student(CommonModel):
    home_group = models.CharField(max_length=10)

    class Meta(CommonModel.Meta):
        db_table = "student_info"
