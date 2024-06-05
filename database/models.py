from django.db import models
from django import forms

class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        labels = {
            'first_name': 'First name :',
            'last_name' : 'Last name :',
            'username' : 'Username :',
            'password' : 'Password :',
        }