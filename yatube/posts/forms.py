from django import forms

class TextForm(forms.Form):
    text = forms.CharField(label="", widget=forms.Textarea, max_length=1024)