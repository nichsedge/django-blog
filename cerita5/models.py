import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

SEMESTER = (
    ("Genap", "Genap"),
    ("Gasal", "Gasal"),
)

class Course(models.Model):
    code = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    lecturer = models.CharField(max_length=100)
    credit = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(24)])
    desc = models.TextField()
    semester = models.CharField(choices=SEMESTER, max_length=5, null=False)
    year = models.PositiveSmallIntegerField()
    room = models.CharField(max_length=20)

    def __str__(self):
        return self.code + " - " + self.name
