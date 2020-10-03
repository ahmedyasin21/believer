from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core import validators
from .models import Contact
from django.core.mail import send_mail

User = get_user_model()

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ["username","email","password1","password2"]
        model = get_user_model()
        widgets ={
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'password1' : forms.TextInput(attrs={'class':'form-control'}),
            'password2' : forms.TextInput(attrs={'class':'form-control'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email is invalid")
        return email
    

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        # self.fields['email'].label = 'Email Address'


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ["from_user","to_user","subject","message",]
        widgets ={
            'from_user' : forms.TextInput(attrs={'class':'form-control'}),
            'to_user' : forms.TextInput(attrs={'class':'form-control'}),
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'message' : forms.Textarea(attrs={'class':'form-control'}),
            }
        
    def clean_users(self):
        from_user = self.cleaned_data["from_user"]
        to_user = self.cleaned_data["to_user"]
        print('this is notice me',from_user)
        print('rhis is 2 notive me',to_user)
        if from_user.endswith('.com') and to_user.endswith('.com'):
            return from_user,to_user
        else:
            raise forms.ValidationError("Email is not correct")
        
   

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField(required=False)
#     class Meta:
#         fields = ["username","email"]




#  for code verifivcation
# class CodeForm(forms.ModelForm):
    
#     vcode = forms.IntegerField(required=True)
#     class Meta:
#         model = Code
#         fields = ("vcode",)

#     def __init__(self,*args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['vcode'].label = 'Verfication Code'

  


