from django import forms
from .models import Signup
from allauth.account.forms import LoginForm


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Type your email address",
    }), label="")

    class Meta:
        model = Signup
        fields = ('email', )

class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].label = False
        self.fields['password'].label = False