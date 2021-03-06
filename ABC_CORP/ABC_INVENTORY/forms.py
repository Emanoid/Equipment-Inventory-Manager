from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['firstName', 'lastName', 'email', 'phone','address','officeLocation','password1', 'password2']

class UploadFileForm(forms.Form):
	file = forms.FileField(required=False)