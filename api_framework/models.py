from django.db import models

# Create your models here.
class testmodel(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    someinteger = models.IntegerField()

    def __str__(self):
        return 'testmodel: {}{}{}'.format(self.firstname, self.lastname, self.someinteger)