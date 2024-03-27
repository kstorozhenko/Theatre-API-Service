from django.contrib import admin


from .models import (
    TheatreHall,
    Genre,
    Actor,
    Play,
    Perfomance,
    Reservation,
    Ticket
)


admin.site.register(TheatreHall)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Play)
admin.site.register(Perfomance)
admin.site.register(Reservation)
admin.site.register(Ticket)