from django.db import models

# Create your models here.
class Heading(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image')
    desc = models.CharField(max_length=200)

class Feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image')

class Government(models.Model):
    image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=50)
    about = models.TextField()
    source = models.CharField(max_length=50)

