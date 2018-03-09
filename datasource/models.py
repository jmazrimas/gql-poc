from django.db import models
# from machine.models import Machine
# from factory.models import Factory


class Datasource(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    machine = models.ForeignKey('Machine', db_column='machine_id', to_field='key', related_name='datasources')

    class Meta:
        app_label = 'gpl_poc'
        managed = False
        db_table = 'datasources'


