from collections.abc import Iterable
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return self

# <HINT> Create a plain Python class `DealerReview` to hold review data


class DealerReview:

    def __init__(self, **kwargs):

        # dealership = kwargs["dealership"]
        # name = kwargs["name"]
        # purchase = kwargs["purchase"]
        # review = kwargs["review"]
        # purchase_date = kwargs["purchase_date"]
        # car_make = kwargs["car_make"]
        # car_model = kwargs["car_model"]
        # car_year = kwargs["car_year"]
        # id = kwargs['id']

        self.dealership = kwargs["dealership"]
        self.name = kwargs["name"]
        self.purchase = kwargs["purchase"]
        self.review = kwargs["review"]
        self.purchase_date = kwargs["purchase_date"]
        self.car_make = kwargs["car_make"]
        self.car_model = kwargs["car_model"]
        self.car_year = kwargs["car_year"]
        self.id = kwargs['id']
        # self.sentiment = kwargs['sentiment']

    def __str__(self):
        return self
        # return " name: " + self['name']


class CarMake(models.Model):
    name = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SUV = "SUV"
    WAGON = "WAGON"
    TYPES = [
        (WAGON, "WAGON"),
        (SUV, "SUV")
    ]

    model = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=200, null=True)
    type = models.CharField(null=False, max_length=30, choices=TYPES)
    year = models.DateField()

    def __str__(self):
        return self.name
