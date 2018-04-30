from django.db import models

# Create your models here.
class City(models.Model):
    #https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/django/models.html
    name = models.CharField(max_length=30)
    temperature = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name
