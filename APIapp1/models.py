from django.db import models

# Create your models here.
class KarthikModel(models.Model):
    name = models.CharField(max_length=10)
    id1 = models.IntegerField()
    salary = models.IntegerField()
    Adress = models.TextField()

    def __str__(self):
        return self.name
