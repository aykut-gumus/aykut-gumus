"""
Skill module
"""
from django.db import models

class Interest(models.Model):
    """
    Interests I have 
    """
    name = models.CharField(max_length=55)
    keywords = models.CharField(max_length=155)

    class Meta:
        ordering = ('name',)
