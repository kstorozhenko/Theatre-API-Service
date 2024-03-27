from django.core.exceptions import ValidationError
from django.db import models

from app import settings


class TheatreHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Actor(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Play(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Perfomance(models.Model):
    show_time = models.DateTimeField()
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-show_time"]

    def __str__(self):
        return self.play.title + " " + str(self.show_time)


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ["-created_at"]


class Ticket(models.Model):
    perfomance = models.ForeignKey(
        Perfomance,
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="tickets",
    )
    row = models.IntegerField()
    seat = models.IntegerField()

    @staticmethod
    def validate_ticket(row, seat, theatre_hall, error_to_raise):
        for ticket_attr_value, ticket_attr_name, theatre_hall_attr_name in[
            (row, "row", "rows"),
            (seat, "seat", "seats_in_row"),
        ]:
            count_attrs = getattr(theatre_hall, theatre_hall_attr_name)
            if not (1 <= ticket_attr_value <= count_attrs):
                raise error_to_raise(
                    {
                        ticket_attr_name: f"{ticket_attr_name}"
                        f"number must be in available range: "
                        f"(1, {theatre_hall_attr_name}):"
                        f"(1, {count_attrs})"
                    }
                )

    def clean(self):
        Ticket.validate_ticket(
            self.row,
            self.seat,
            self.perfomance.theatre_hall,
            ValidationError,
        )

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None
    ):
        self.full_clean()
        return super(Ticket, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self):
        return (
            f"{str(self.perfomance)} (row: {self.row}, seat: {self})"
        )

    class Meta:
        unique_together = ("movie_session", "row", "seat")
        ordering = ["row", "seat"]