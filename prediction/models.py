from django.db import models

# Create your models here.
class TrainData(models.Model):
    cement = models.FloatField()
    blast_furnace_slag = models.FloatField()
    fly_ash = models.FloatField()
    water = models.FloatField()
    superplasticizer = models.FloatField()
    coarse_aggregate = models.FloatField()
    fine_aggregate = models.FloatField()
    age = models.IntegerField()
    strength = models.FloatField()
    
    def __str__(self):
        return self.cement