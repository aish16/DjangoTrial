from django.db import models

# Create your models here.




class Department(models.Model):
        Dept_name=models.CharField(max_length=100)
        Dept_head=models.CharField(max_length=100)
        def __str__(self):
                return self.Dept_name


class Employee(models.Model):
        Employee_name=models.CharField(max_length=250)
        Emp_pic=models.CharField(max_length=1000)
        Dept=models.ForeignKey(Department,on_delete=models.CASCADE)
        def __str__(self):
                return self.Employee_name

class Project(models.Model):
        start_date=models.CharField(max_length=50)
        end_date=models.CharField(max_length=50)
        project_name=models.CharField(max_length=250)
        supervisor_name=models.ForeignKey(Employee,on_delete=models.CASCADE)
