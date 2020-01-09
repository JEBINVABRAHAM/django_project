from django.db import models

# Create your models here.

class student (models.Model):
    studentid=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=40,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=10,null=True,blank=True)
    mobileno=models.IntegerField(null=True,blank=True)
    admissiondate=models.DateField(null=True,blank=True)
    guardian=models.CharField(max_length=10,null=True,blank=True)
    batch=models.CharField(max_length=10,null=True,blank=True)
    email=models.EmailField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)

    
class faculty (models.Model):
   facultyid=models.IntegerField(primary_key=True) 
   username=models.CharField(max_length=20,null=True,blank=True)
   address=models.CharField(max_length=40,null=True,blank=True)
   dob=models.DateField(null=True,blank=True)
   gender=models.CharField(max_length=10,null=True,blank=True)
   qualification=models.CharField(max_length=20,null=True,blank=True)
   batchincharge=models.CharField(max_length=20,null=True,blank=True)
   email=models.CharField(max_length=20,null=True,blank=True)
   mobileno=models.IntegerField(null=True,blank=True)
   password=models.CharField(max_length=20,null=True,blank=True)

class facultyattendance (models.Model):
    date=models.DateField()
    facultyid=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20,null=True,blank=True) 
    status_hour1=models.CharField(max_length=10)
    status_hour2=models.CharField(max_length=10)
    status_hour3=models.CharField(max_length=10)
    status_hour4=models.CharField(max_length=10)

class sattendance (models.Model):
    date=models.DateField(null=True,blank=True)
    username=models.CharField(max_length=20,null=True,blank=True)
    studentid=models.IntegerField()
    status_hour1=models.CharField(max_length=10)
    status_hour2=models.CharField(max_length=10)
    status_hour3=models.CharField(max_length=10)
    status_hour4=models.CharField(max_length=10)

class marks (models.Model):
    studentid=models.IntegerField()
    username=models.CharField(max_length=20,null=True,blank=True)
    assesmentno=models.IntegerField()
    sub1=models.CharField(max_length=20)
    sub2=models.CharField(max_length=20)
    sub3=models.CharField(max_length=20)
    percentage=models.IntegerField()

class admin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class studentleave (models.Model):
    username=models.CharField(max_length=20,null=True,blank=True)
    batch=models.CharField(max_length=10,null=True,blank=True) 
    fromdate=models.DateField()
    todate=models.DateField()
    reason=models.CharField(max_length=40,null=True,blank=True)
    status=models.CharField(max_length=10)

class facultyleave (models.Model):
    username=models.CharField(max_length=20,null=True,blank=True)
    fromdate=models.DateField()
    todate=models.DateField()
    reason=models.CharField(max_length=40,null=True,blank=True)
    status=models.CharField(max_length=10)
   







class Meta:
    db_table='sign'
    db_table='student'
    db_table='faculty'
    db_table='facultyattendance'
    db_table='sattendance'
    db_table='marks'
    db_table='admin'
    db_table='studentleave'
    db_table='facultyleave'
    