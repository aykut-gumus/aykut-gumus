"""
Contact module
"""
from django.db import models

class Contact(models.Model):
    """
    Contact methods
    """
    method = models.CharField(max_length=10)
    value = models.CharField(max_length=155)
