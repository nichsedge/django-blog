from django.db import models


# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    member = models.ManyToManyField(Member, blank=True)

    def __str__(self):
        return self.title


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=27)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
