"""
Skill module
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Skill(models.Model):
    """
    Individual, technical skills
    """
    name = models.CharField(max_length=55)
    rank = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(5)])

    class Meta:
        ordering = ('rank', 'name',)
