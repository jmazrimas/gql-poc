from django.db import models
from machine.models import Machine


# class Factory(models.Model):
#     name = models.CharField()
#     # machines = models.OneToManyField(Machine)
#
#     class Meta:
#         app_label = 'gpl_poc'
#         managed = False
#         db_table = 'factory'


class Factory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # machines = models.ForeignKey('Machine')

    class Meta:
        app_label = 'gpl_poc'
        managed = False
        db_table = 'factory'