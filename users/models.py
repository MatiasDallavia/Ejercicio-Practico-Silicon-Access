from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

from vehicles.models import Vehicle


class PrivateArea(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    allowed_vehicles_type = ArrayField(
        models.CharField(
            choices=Vehicle.VEHICLE_TYPES_CHOISES, default="CAR", max_length=25, null=False
        )
    )
    city = models.CharField(max_length=25, null=False)
