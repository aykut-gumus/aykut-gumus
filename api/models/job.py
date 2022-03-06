"""
Job module
"""
from django.db import models

class Job(models.Model):
    """
    Information about each job
    """
    organization = models.CharField(max_length=55)
    role = models.CharField(max_length=55)
    start_year = models.DateField()
    end_year = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    synopsis = models.TextField()

    def __str__(self):
        return "{} at {}".format(self.role, self.organization)

    class Meta:
        ordering = ('start_year',)
