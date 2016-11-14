from django import forms

class UserForm(forms.Form):
    Input_Email = forms.CharField(label='Input Email', max_length=200)
    Input_Password = forms.CharField(label='Input Password', max_length=100)
