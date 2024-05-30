from django import forms
class usersforms(forms.Form):
    num1=forms.CharField(label="value1", required=False,widget=forms.TextInput(attrs={'class': "form-control"})) 
    num2=forms.CharField(label="value2", required=False,widget=forms.TextInput(attrs={'class': "form-control"})) 
    num3=forms.CharField(label="value3", required=False,widget=forms.Textarea(attrs={'class': "form-control"})) 
    email=forms.EmailField()