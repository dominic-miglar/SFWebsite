from django.db import models
import datetime


# Create your models here.


class Member(models.Model):
    firstName = models.CharField("Vorname", max_length=200)
    lastName = models.CharField("Nachname", max_length=200)
    job = models.CharField("Beruf", max_length=200)
    photoPath = models.ImageField("Foto", upload_to='images/photos/members')
    email = models.EmailField("E-Mail", max_length=75)
    
    def __unicode__(self):
       return '%s %s' % (self.firstName, self.lastName)


class Car(models.Model):
    member = models.ForeignKey(Member)
    brand = models.CharField("Hersteller", max_length=200)
    model = models.CharField("Modell", max_length=200)
    photoPath = models.ImageField("Foto", upload_to='images/photos/cars')
    horsePower = models.IntegerField("PS") 
    cylinderCapacity = models.FloatField("Hubraum (Liter)")
    otherInfos = models.TextField("Sonstige Informationen")    

    def __unicode__(self):
        return '%s %s' % (self.brand, self.model)


class Newsarticle(models.Model):
    title = models.CharField("Titel", max_length=100)
    pub_date = models.DateTimeField("Publi- zierungs- datum")     #auto_now_add=True)
    header = models.CharField("Ueberschrift", max_length=200)
    body = models.TextField("Text") # fuer das waere tinymce geil :D

    def __unicode__(self):
        return self.title


class Sponsor(models.Model):
    name = models.CharField("Name", max_length=200)
    sponsored = models.CharField("Sponsored", max_length=200)
    descr = models.TextField("Informationen")
    banner = models.ImageField("Banner", upload_to='images/banners')
    otherInfos = models.TextField("Sonstiges")
    website = models.URLField("Webseite")


    def __unicode__(self):
        return self.name

#impressum statisch!
#menue items statisch !!!!!!
