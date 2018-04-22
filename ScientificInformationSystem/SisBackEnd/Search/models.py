from django.db import models

# Create your models here.

#作者表
class authors(models.Model):
    uniid = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    organization = models.CharField(max_length=30)
    avatar_src = models.CharField(max_length=120)
    work_experience = models.CharField(max_length=50)
    edu_experience = models.CharField(max_length=50)
    domain = models.CharField(max_length=60)
    intro = models.CharField(max_length=100)
    def __unicode__(self):
        return self.authors

class paper(models.Model):
    author1_uniid = models.CharField(max_length=30)
    author2_uniid = models.CharField(max_length=30)
    author3_uniid = models.CharField(max_length=30)
    author4_uniid = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=30)
    key_words = models.CharField(max_length=50)
    abstract = models.CharField(max_length=200)
    source = models.CharField(max_length=50)
    document_type_sign = models.CharField(max_length=30)
    journal = models.CharField(max_length=50)