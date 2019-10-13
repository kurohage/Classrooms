from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	#def get_absolute_url(self):
	#	return reverse('classroom-detail', kwargs={'classroom_id':self.id})

	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	# gender choices: first field is the DB data, and the 2nd is the form display
	gender = models.CharField(choices=(("Male","Male"), ("Female","Female")), max_length=6)
	exam_grade = models.FloatField()
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE) # delete students when the class is deleted

	#def get_absolute_url(self):
		#return reverse('student:detail', kwargs={'student_id': self.id})

	def __str__(self):
		return self.name
