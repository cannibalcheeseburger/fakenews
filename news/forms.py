from django import forms

class NewsForm(forms.Form):
    query = forms.CharField(label='News Snippet', max_length=500)