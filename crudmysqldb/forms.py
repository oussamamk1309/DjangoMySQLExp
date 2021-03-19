from django import forms
from crudmysqldb.models import Students, Employes

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

class EmployesForm(forms.ModelForm):
    class Meta:
        model = Employes
        fields = "__all__"

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=256)
    