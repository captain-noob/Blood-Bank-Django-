from django.db import models

# Create your models here.

class login(models.Model):
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    user_role= models.CharField(max_length=100)
    status= models.IntegerField()

class bloodgroup(models.Model):
    name = models.CharField(max_length=10)

class donerreg(models.Model):
    name  = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.DateField()
    phone=models.CharField(max_length=20)
    bloodgroup=models.ForeignKey(bloodgroup)
    weight=models.IntegerField()
    status = models.IntegerField()
    login = models.ForeignKey(login)

class accepterreg(models.Model):
    name= models.CharField(max_length=100)
    address_bio= models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    phone= models.CharField(max_length=20)
    bloodgroup= models.ForeignKey(bloodgroup)
    status=models.IntegerField()
    login= models.ForeignKey(login)

class donerstatus(models.Model):
    dateofdonation = models.DateField()
    center=models.CharField(max_length=20)
    login = models.ForeignKey(login)

class sendrequest(models.Model):
    requestdate=models.DateField()
    accepterreg=models.ForeignKey(accepterreg)
    donerreg=models.ForeignKey(donerreg)


