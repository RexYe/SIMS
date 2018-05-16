from django.db import models
import hashlib
# Create your models here.

#作者表
class authors(models.Model):
    uniid = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    organization = models.CharField(max_length=30)
    avatar_src = models.CharField(max_length=200)
    work_experience = models.CharField(max_length=250)
    edu_experience = models.CharField(max_length=250)
    domain = models.CharField(max_length=60)
    intro = models.CharField(max_length=100)
    def __unicode__(self):
        return self.authors

class paper_title(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publish_time = models.CharField(max_length=60)
    journal = models.CharField(max_length=200)
    authors_uniid = models.CharField(max_length=200)
    def __unicode__(self):
        return self.paper_title

class paper_detail(models.Model):
    abstract = models.CharField(max_length=600)
    authors = models.CharField(max_length=200)
    key_words = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    src = models.CharField(max_length=200)
    authors_uniid = models.CharField(max_length=200)
    def __unicode__(self):
        return self.paper_detail

class journal(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    introduction = models.CharField(max_length=800)
    category = models.CharField(max_length=30)
    logo = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    host_unit = models.CharField(max_length=100)
    influence = models.CharField(max_length=20)
    honor = models.CharField(max_length=50)
    def __unicode__(self):
        return self.journal