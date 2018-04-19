from django.db import models

# Create your models here.



class authors(models.Model):
    uniid = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    organization = models.CharField(max_length=30)
    def __unicode__(self):
        return self.authors
