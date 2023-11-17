from django import forms

from crm.models import Employees

from django.contrib.auth.models import User

class EmployeeForm(forms.Form):
    name=forms.CharField()
    department=forms.CharField()
    salary=forms.IntegerField()
    email=forms.EmailField()
    age=forms.IntegerField()
    contact=forms.CharField()

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control border border-light-subtle"}),
            "department":forms.TextInput(attrs={"class":"form-control border light-subtle"}),
            "salary":forms.NumberInput(attrs={"class":"form-control border light-subtle"}),
            "email":forms.EmailInput(attrs={"class":"form-control border light-subtle"}),
            "age":forms.NumberInput(attrs={"class":"form-control border light-subtle"}),
            "contact":forms.Textarea(attrs={"class":"form-control border light-subtle   ","rows":5}),
            "dob":forms.DateInput(attrs={"class":"form-control border light-subtle","type":"date"})



        }


class RegistrationForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["username","email","password"]


class LoginForm(forms.Form):
        username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-light-subtle"}))
        password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-light-subtle"}))

    
    