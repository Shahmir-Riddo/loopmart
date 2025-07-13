from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile
from crispy_forms.helper import FormHelper



class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'


        
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    mobile_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_number', 'password1', 'password2']

    def clean_mobile_number(self):
        mobile = self.cleaned_data.get('mobile_number')
        if mobile and len(mobile) != 11:
            raise forms.ValidationError("Mobile number must be exactly 11 digits")
        return mobile

    def save(self, commit=True):
        user = super().save(commit=commit)
        mobile = self.cleaned_data.get('mobile_number')

        if commit:
            Profile.objects.filter(user=user).update(mobile_number=mobile)