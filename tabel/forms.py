from django import forms
from dvsr.models import Employerxpo

employeesSelection = Employerxpo.objects.all()

class EmployeeSelectForm(forms.Form):
    selectEmployee = forms.MultipleChoiceField(choices = employeesSelection)