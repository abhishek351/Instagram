from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import *


class Signupform(UserCreationForm):
    username   = forms.CharField(widget=(forms.TextInput(attrs={'class': 'signup-form', 'placeholder': 'Username',})),label='')
    first_name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'signup-form', 'placeholder': 'First Name',})),label='', max_length=32)
    last_name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'signup-form', 'placeholder': 'Last Name',})),label='', max_length=32)
    email      = forms.EmailField(widget=(forms.EmailInput(attrs={'class': 'signup-form', 'placeholder': 'Email',})),label='', max_length=64)
    password1  = forms.CharField(widget=(forms.PasswordInput(attrs={'class': 'signup-form', 'placeholder': 'Password',})),label='')
    password2  = forms.CharField(widget=(forms.PasswordInput(attrs={'class': 'signup-form', 'placeholder': 'Password Again',})),label='')

        

       

    class Meta:
        model = User
        fields = ('email', 'first_name','last_name','username', 'password1','password2')


class loginform(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(loginform, self).__init__(*args, **kwargs)
        
    username = forms.CharField(widget=(forms.TextInput(attrs={'class': 'signup-form','placeholder':'Username'})),label='')
    password = forms.CharField(widget=(forms.PasswordInput(attrs={'class': 'signup-form','placeholder':'Password'})),label='')


    
    class Meta:
        model=User
        fields ="__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model =post
        fields=('photo','caption')
        widgets={
            'caption':forms.TextInput(attrs={'placeholder':'Add a Caption..','size': 40,'class':'post-create-form'})
        }




    



class UserUpdateform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']


    def __init__(self, *args, **kwargs):
        super(UserUpdateform, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'user-edit-form','placeholder': 'Name'},)
        self.fields['first_name'].label = 'Name'
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'user-edit-form','placeholder': 'Username'},)
        self.fields['username'].help_text = None
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'user-edit-form','placeholder': 'Email'},)
        self.fields['email'].label = 'Email'
   



class ProfileUpdateform(forms.ModelForm):
    class Meta:
            model=profile
            fields=['photo','website','bio']  

    def __init__(self, *args, **kwargs):
            super(ProfileUpdateform, self).__init__(*args, **kwargs)

            self.fields['website'].widget = forms.TextInput(attrs={'class': 'user-edit-form','placeholder': 'Website'},)
            self.fields['bio'].widget = forms.TextInput(attrs={'class': 'user-edit-form','placeholder': 'Bio'},)
            

class passwordChangeForm(PasswordChangeForm):


    def __init__(self, *args, **kwargs):
        super(passwordChangeForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget = forms.TextInput(attrs={'class': 'user-edit-form','placeholder': 'Old-Passoword'},)
        
        self.fields['new_password1'].widget = forms.TextInput(attrs={'class': 'user-edit-form','placeholder': 'New Password'},)
        self.fields['new_password2'].widget = forms.TextInput(attrs={'class': 'user-edit-form','placeholder': 'Re-enter NewPassword '},)
    


        