from django.db import models



class Employee(models.Model):
    fName=models.CharField(max_length=10)
    lName=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    def __str__(self):
        return self.fName