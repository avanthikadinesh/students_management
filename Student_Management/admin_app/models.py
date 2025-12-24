from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_name=models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.teacher_name} ({self.subject})"
    

class Subject(models.Model):
    subject_name = models.CharField(max_length=100) 
    code = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.subject_name}"
    

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    course=models.CharField(max_length=50)
    register_num=models.IntegerField()
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
    subject=models.ManyToManyField(Subject)


class Profile(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    address = models.CharField(max_length=200) 
    phone = models.CharField(max_length=15)

   



