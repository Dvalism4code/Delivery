from django import forms
from .models import ContactForm


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'phone', 'message', 'subject']

