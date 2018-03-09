from django.db import models


class Machine(models.Model):
    id = models.IntegerField()
    key = models.CharField()
    name = models.CharField()
    factory = models.ForeignKey('Factory', related_name='machines')

    class Meta:
        app_label = 'gpl_poc'
        managed = False
        db_table = 'machines'
