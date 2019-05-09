from django.db import models

class Recruit(models.Model):
    company_name = models.CharField(max_length=50)
    recruiter_name = models.CharField(max_length=50)
    job_content = models.TextField()
    publish_data = models.DateField(auto_now=True, auto_now_add=True)