from django.db import models
from machine.models import Machine


class Factory(models.Model):
    name = models.CharField()
    # machines = models.OneToManyField(Machine)

    class Meta:
        app_label = 'gpl_poc'
        managed = False
        db_table = 'factory'
