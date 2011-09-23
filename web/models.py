from django.db import models
import datetime


# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    photoPath = models.ImageField(upload_to='images/photos/members')
    
    def __unicode__(self):
       return self.name


class Car(models.Model):
    member = models.ForeignKey(Member)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    photoPath = models.ImageField(upload_to='images/photos/cars')
    horsePower = models.IntegerField() 
    otherInfos = models.TextField()
   
    def __unicode__(self):
        return '%s %s' % self.brand, self.model


class Newsarticle(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    header = models.CharField(max_length=200)
    body = models.TextField() # fuer das waere tinymce geil :D

    def __unicode__(self):
        return self.title


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    sponsored = models.CharField(max_length=200)
    descr = models.TextField()
    banner = models.ImageField(upload_to='images/banners')

    def __unicode__(self):
        return self.name

#impressum statisch!
#menue items statisch !!!!!!
