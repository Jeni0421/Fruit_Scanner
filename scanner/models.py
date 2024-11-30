from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    health_benefits = models.TextField()
    common_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name