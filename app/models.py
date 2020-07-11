from django.db import models

# Create your models here.


class form(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    aadhaar = models.IntegerField()
    char_id = models.IntegerField()
    in_game = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class url(models.Model):
    aadhaar = models.IntegerField()
    name = models.CharField(max_length=100)
    imageurl = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
