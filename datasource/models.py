from django.db import models
# from machine.models import Machine


class Datasource(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    # machine = models.OneToOneField(Machine)
    # machine = models.ForeignKey(Machine, db_column='machine_id')

    class Meta:
        app_label = 'gpl_poc'
        managed = False
        db_table = 'datasources'


