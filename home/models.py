from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class dishes(models.Model):
    dish_id = models.AutoField
    dish_name = models.CharField(max_length=122)
    category = models.CharField(max_length=122)
    image = models.ImageField(upload_to='home/images')
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.dish_name

