from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import CharField


class Classroom(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    year = models.IntegerField()
    teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE , related_name='classrooms')

    def get_absolute_url(self):
        return reverse('classroom-detail', kwargs={'classroom_id':self.id})

gender_option=(
        ('Male' , 'male'),
        ('Female' , 'Female')

    )
class Student(models.Model):
    name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=gender_option)
    exam_grade = models.FloatField()
    classroom = models.ForeignKey(Classroom, default=1, on_delete=models.CASCADE , related_name='students')