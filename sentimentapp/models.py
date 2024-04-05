from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Usertable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    photo = models.FileField()

class Feedback(models.Model):
    feedback = models.CharField(max_length=800)
    date = models.DateField()
    USER = models.ForeignKey(Usertable, on_delete=models.CASCADE)


class Complaint(models.Model):
    complaint = models.CharField(max_length=800)
    reply = models.CharField(max_length=800)
    USER = models.ForeignKey(Usertable, on_delete=models.CASCADE)
    date = models.DateField()

class Review(models.Model):
    product=models.CharField(max_length=100)
    review=models.CharField(max_length=5000)
    positive=models.CharField(max_length=50)
    negative=models.CharField(max_length=50)
    nuetral=models.CharField(max_length=50)
    date=models.DateField()