from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from send_mail.models import Information, TakeEmail
from django import forms

class TakeEmailCreateForm(forms.ModelForm):
    class Meta:
        model = TakeEmail
        fields = ['recepient_email']

class InformationCreateForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['product_name', 'Category', 'Qty', 'price']


class UserEmail(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email
