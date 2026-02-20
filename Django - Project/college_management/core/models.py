from django.db import models

# Create your models here.
# Schema for Student Module
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    usn = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=50)
    sem = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    # Foreign Key reference is used for enrolling the student with a course
    # on_delete conscade is going to remove all the dependency on other tables
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # We will update Current Timestamp
    date_enrolled = models.DateField(auto_now_add=True)