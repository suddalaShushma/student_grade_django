from django.db import models
# students/models.py
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    def __str__(self):
        return self.name

