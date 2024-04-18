from django.db import models

# Create your models here.


class Airline(models.Model):
    date = models.DateField()
    destination = models.TextField()
    passenger = models.TextField()
    bags = models.PositiveIntegerField(null=True, default=0)
    first_class = models.BooleanField(default=False)

def create_ticket(date, destination, passenger, bags, first_class):
    airline = Airline(date=date, destination=destination, passenger=passenger, bags=bags, first_class=first_class)
    airline.save()
    return airline

def find_ticket(id):
    ...

def all_tickets():
    return Airline.objects.all()

def upgrade_first_class(passenger):
    name = Airline.objects.get(passenger=passenger)
    name.first_class = True
    name.save()
    return name

def delete_ticket(passenger):
    name = Airline.objects.get(passenger=passenger)
    name.delete()