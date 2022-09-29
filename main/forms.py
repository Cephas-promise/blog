from email.policy import default
from tkinter import Widget
from django import forms
from.models import post, profile
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registrationform(UserCreationForm):
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name', 'email', 'password1', 'password2')
       
    



class addpostform(forms.ModelForm):
    class Meta:
        model=post
        fields=('author','title','title_tags', 'body', 'email',)

        widgets={
           # "author": forms.select(attrs={'class':'form-control',"value":"", 'id':'user', 'type':'hidden'}),
           "author": forms.TextInput(attrs={'class':'form-control',"value":"", 'id':'user', 'type':'hidden'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tags': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'body'}),
            "email": forms.TextInput(attrs={'class':'form-control',"value":"", 'id':'email', 'type':'hidden'}),
            #'phoneno': forms.TextInput(attrs={'class':'form-control',"value":"", 'id':'phoneno', 'type':'hidden'}),


        }

        







class updateuserform(forms.ModelForm):
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=30,  widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name', 'email',)
       
        

#class editpostform (forms.ModelForm):
 #   class Meta:
  #      models=post
   #     fields=('title', 'body')

class profileupdate(forms.ModelForm):
    class Meta:
        model=profile
        fields=('phone_number','bio', 'image')
        widgets ={
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control',}),
            #'image':forms.ImageField(attrs={'class':'form-control'}),
            #'password':forms.PasswordInput(attrs={'class':'form-control',}),

        }

        