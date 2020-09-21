from django import forms
from django.utils.safestring import mark_safe


class DeclineReasonForm(forms.Form):
    decline_reason = forms.CharField(label='', widget=forms.Textarea)
