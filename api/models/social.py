"""
Social module
"""
from django.db import models

class Social(models.Model):
    """
    Stores name and link for social media
    """
    organization = models.CharField(max_length=55)
    link = models.CharField(max_length=155)
