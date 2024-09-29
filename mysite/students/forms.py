# students/forms.py

from django import forms
from .models import Student
#class StudentForm(forms.Form):
   # name = forms.CharField(max_length=100)
   # age = forms.IntegerField()
    #bio = forms.CharField(widget=forms.Textarea)
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'bio']