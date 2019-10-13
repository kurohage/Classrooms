from django import forms
from .models import Classroom, Student
from django.contrib.auth.models import User

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        #fields = '__all__' # mutually exclusive with exclude. No need to define it when exclude is used.
        exclude = ['teacher',]

        #widgets = {
        #	'year': forms.DateInput(attrs={'format':'%Y'}),
        #}

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['classroom']

        widgets = {
        	'date_of_birth': forms.DateInput(attrs={'type':'date'}),
        }

class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email' ,'password']

		widgets={
        'password': forms.PasswordInput(),
        }

class SigninForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())