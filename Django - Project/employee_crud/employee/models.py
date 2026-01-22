from django.db import models

# Create your models here.
class Employee(models.Model):
    DEPT_CHOICES = [
     ('Dev Team', 'Development Team'),
     ('QA Team', 'Quality Assurance Team'),
     ('DevOPS Team', 'Deployment Team')
    ]

    ROLE_CHOICES = [
     ('Trainee', 'Trainee Engineer'),
     ('ASE', 'Associate Software Engineer'),
     ('ASD', 'Assisstant Software Developer'),
     ('SSD', 'Senior Software Developer'),
     ('QA', 'QA Engineer')
    ]

    GENDER_CHOICES = [
     ('M', 'Male'),
     ('F', 'Female'),
     ('O', 'Others')
    ]

    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email_id = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    dept = models.CharField(max_length=20, choices=DEPT_CHOICES)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name