from django.db import models
# from datasource.models import Datasource

class Machine(models.Model):
    id = models.IntegerField()
    key = models.CharField()
    factory_id = models.IntegerField()
    name = models.CharField()

    class Meta:
        app_label = 'gpl_poc'
        managed = False
        db_table = 'machines'