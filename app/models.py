from django.db import models
from .baseModel import BaseModel
from datetime import datetime

# Create your models here.
class Department(BaseModel):
    name = models.CharField(max_length=50,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name

class Instructor(BaseModel):
    name                = models.CharField(max_length=100,null=True,blank=True)
    email               = models.CharField(max_length=100,null=True,blank=True)
    tag                 = models.CharField(max_length=100,null=True,blank=True)
    address             = models.CharField(max_length=100,null=True,blank=True)
    description         = models.TextField(null=True,blank=True)
    gender              = models.CharField(max_length=100,null=True,blank=True)
    department          = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    rank                = models.CharField(max_length=100,null=True,blank=True)
    firstShift          = models.CharField(max_length=10,null=True,blank=True)  
    secondShift         = models.CharField(max_length=10,null=True,blank=True)  
    instructorImage     = models.ImageField(upload_to="instructorImage",blank=True,null=True)
    def __str__(self):
        return self.name
    
class Student(BaseModel):
    name                = models.CharField(max_length=100,null=True,blank=True)
    roll                = models.CharField(max_length=100,null=True,blank=True)
    email               = models.CharField(max_length=100,null=True,blank=True)
    went                = models.CharField(max_length=100,null=True,blank=True)
    address             = models.CharField(max_length=100,null=True,blank=True)
    description         = models.TextField(null=True,blank=True)
    gender              = models.CharField(max_length=100,null=True,blank=True)
    department          = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    cr                  = models.CharField(max_length=10,null=True,blank=True)   
    firstShift          = models.CharField(max_length=10,null=True,blank=True)  
    secondShift         = models.CharField(max_length=10,null=True,blank=True)  
    studentImage        = models.ImageField(upload_to="studentImage",blank=True,null=True)
    def __str__(self):
        return self.name
    

class Instrument(BaseModel):
    name                = models.CharField(max_length=100,null=True,blank=True)
    closet              = models.CharField(max_length=100,null=True,blank=True)
    rack                = models.CharField(max_length=100,null=True,blank=True)
    department          = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    instrumentImage     = models.ImageField(upload_to="instrumentImage",blank=True,null=True)
    def __str__(self):
        return self.name
    

class Notice(BaseModel):
    heading             = models.CharField(max_length=300,null=True,blank=True)
    details             = models.TextField(null=True,blank=True)
    noticeImage         = models.ImageField(upload_to="noticeImage",blank=True,null=True)
    def __str__(self):
        return self.heading
    