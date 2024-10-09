# employee/models.py
from django.db import models

class Employee(models.Model):
    # Basic employee details
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)

    # Set default value for address_details to an empty dict
    address_details = models.JSONField(default=dict)

    # Work experience as a list of dictionaries
    work_experience = models.JSONField(default=list)

    # Qualifications as a list of dictionaries
    qualifications = models.JSONField(default=list)

    # Projects as a list of dictionaries
    projects = models.JSONField(default=list)

    def __str__(self):
        return self.name
