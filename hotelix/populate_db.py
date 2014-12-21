# -*- coding: utf-8 -*-
import os
from random import random, sample, randint

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelix.settings")

django.setup()

from client.models import Client, Order
from structure.models import House, Floor, Chamber, Room
# from .services.models import MealType, ServiceType


def add_client(name, phone_number, address, desc):
    ## created = models.DateTimeField(u"Utworzono", auto_now_add=True)
    ## name = models.CharField(u"Imię i nazwisko", max_length=100)
    ## telephone = models.CharField(u"nr tel.", max_length=20, validators=[phone_regex], blank=True)
    ## address = models.TextField(u"Adres", blank=True)
    ## description = models.TextField(u"Opis", blank=True)
    client = Client.objects.get_or_create(name=name, telephone=phone_number,
                                          address=address, description=desc)
    return client


def add_order(rooms, number_of_people, number_of_disabled,
              arrival_time,  departure_time, price_per_night, client):
    ## rooms = models.ManyToManyField(Room, null=False)
    ## number_of_people = models.IntegerField(u"Liczba gości", null=False)
    ## number_of_disabled = models.IntegerField(u"Liczba niepełnosprawnych", null=False, default=0)
    ## arrival_time = models.DateTimeField(u"Data przyjazdu", null=False)
    ## departure_time = models.DateTimeField(u"Data wyjazdu", null=False)
    ## price_per_night = models.DecimalField(u"Cena za noc", max_digits=10, decimal_places=2, null=False)
    ## client = models.ForeignKey(Client, null=False)
    order = Order.objects.get_or_create(rooms, number_of_people,
                                        number_of_disabled,
                                        arrival_time,
                                        departure_time,
                                        price_per_night,  client)[0]
    return order


def add_house(name):
    ## name = CharField(u"Nazwa budynku", max_length=50, null=False, blank=False)
    house = House.objects.get_or_create(name=name)[0]
    return house


def add_floor(number, house):
    ## number = models.IntegerField(u"Numer piętra", null=False, blank=False)
    ## house = models.ForeignKey(House, null=False)
    floor = Floor.objects.get_or_create(number=number, house=house)[0]
    return floor


def add_room(beds, name, for_disabled, floor):
    ## beds = IntegerField(u"Liczba miejsc", null=False, blank=False)
    ## name = CharField(u"Nazwa", max_length=10, null=False, blank=False, default='')
    ## for_disabled = BooleanField(u"Dla niepełnosprawnych", default=False)
    ## floor = ForeignKey(Floor, null=False)
    room = Room.objects.get_or_create(beds=beds, name=name,
                                      for_disabled=for_disabled, floor=floor)[0]
    return room


def add_chamber(description, house):
    chamber = Chamber.objects.get_or_create(description=description,
                                            house=house)[0]
    return chamber


def populate():
    ## create infrastructure
    buildings = [u"Błękitek", u"Dar Pomorza", u"WTC"]
    chambers = [u"PingPong", u"Oranżeria", u"Kino", u"Kaplica"]

    max_floors_no = 3
    max_rooms_no = 6
    max_beds_no = 4

    def choose_nonzero_rnd(max_rnd):
        return randint(1, max_rnd)

    for building in buildings:
        house = add_house(name=building)
        ## choose non-zero pseudo-random number
        floors_no = choose_nonzero_rnd(max_floors_no)
        for number in range(floors_no):
            floor = add_floor(number, house)
            rooms_no = choose_nonzero_rnd(max_rooms_no)
            for rno in range(1, rooms_no):
                beds_no = choose_nonzero_rnd(max_beds_no)
                ## we need slightly more regular rooms
                disabled =  bool(round(random() - 0.3))
                add_room(beds_no, '', disabled, floor)
        ## now add some chamber
        choices = sample(range(len(chambers) + 1), randint(0, len(chambers)))
        for choice in choices:
            add_chamber(chambers[choice], house)

    ## populate DB with clients
    first_names = [u"Anita", u"Adam", u"Bernard", u"Beata", u"Zdzisia",
                   u"Żaneta", u"John", u"Josh"]
    second_names = [u"Kęss", u"Mann", u"Wolarz", u"Maluch", u"Pędziwiatr",
                   u"Winiaczek", u"Karp", u"Browar", u"Pong"]

    for first_name in first_names:
        for surname in second_names:
            full_name = first_name + " " + surname
            phone_number = str(int(random()*10**(randint(9,15))))
            add_client(full_name, phone_number, '', '')
    return


if __name__ == "__main__":
    populate()
