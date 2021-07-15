from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class NewsForm(forms.Form):
    query = forms.CharField(label='News Snippet', max_length=500)

    
class NewNewsForm(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    text = forms.CharField(label='text', max_length=500)