from django.db import models

# Create your models here.
class testrawmodel(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    someinteger = models.IntegerField()

    def __str__(self):
        return 'testrawmodel: {}{}{}'.format(self.firstname, self.lastname, self.someinteger)