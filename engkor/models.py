from django.db import models

class Definition(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.TextField()
    definition = models.TextField()

    class Meta:
        db_table = 'definitions'
        managed = False