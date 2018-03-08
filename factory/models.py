from django.db import models


class Factory(models.Model):
    name = models.CharField()

    class Meta:
        app_label = 'gpl_poc'
        managed = False
        db_table = 'factory'