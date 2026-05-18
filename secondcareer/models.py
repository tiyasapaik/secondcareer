from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Secondcareer(models.Model):
    company_name=models.CharField(max_length=100)
    job_description=models.TextField()
    job_image=models.ImageField(upload_to="secondcareer")

    def __str__(self):
        return self.company_name
