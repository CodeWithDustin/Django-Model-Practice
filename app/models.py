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
    return Airline.objects.get(id=id)

def all_tickets():
    return Airline.objects.all()

def upgrade_first_class(id):
    ticket = find_ticket(id)
    if not ticket.first_class:
        ticket.first_class = True
        ticket.save()
        return ticket
    else:
        raise ValueError

def delete_ticket(id):
    name = Airline.objects.filter(id=id)
    name.delete()

def tickets_by_destination(destination):
    place = Airline.objects.filter(destination=destination)
    return place

def tickets_by_first_class():
    first = Airline.objects.filter(first_class=True)
    return first

def update_bags(id, bags):
    ticket = Airline.objects.get(id=id)
    ticket.bags = bags
    ticket.save()
    return ticket