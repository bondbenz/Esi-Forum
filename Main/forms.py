from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

ROLE = (
        ('etudiant', 'Etudiant'),
        ('enseignant', 'Enseignant'),
    )

ROLE1=(
    ('etudiant', 'Etudiant'),
    ('enseignant', 'Enseignant'),
    ('moderateur','Moderateur')
)

ROLE2=(
    ('All','All'),
    ('etudiant', 'Etudiant'),
    ('enseignant', 'Enseignant'),
    ('moderateur','Moderateur'),
    
)

PROMO = (
        ('1cpi', '1CPI'),
        ('2cpi', '2CPI'),
        ('1cs', '1CS'),
        ('2cs', '2CS'),
        ('3cs', '3CS'),
    )

class SignUpForm(UserCreationForm):

    phone_number=forms.CharField(max_length=10,required=False,label="Phone Number")
    bio =forms.CharField(widget=forms.Textarea,required=False)
    role =forms.ChoiceField(choices = ROLE, label="", initial='', widget=forms.Select(), required=True)
    promo= forms.ChoiceField(choices = PROMO, label="", initial='', widget=forms.Select(), required=True)

    class Meta:
        model = Utilisateur
        fields = ('first_name', 'last_name', 'username', 'email','phone_number', 'password1', 'password2', 'role','promo','bio')



class userUpdate(forms.Form):
    username=forms.CharField(required=False)
    username1=forms.CharField(required=False)
    role =forms.ChoiceField(choices = ROLE1, label="", initial='', widget=forms.Select(), required=False)
    password =forms.CharField(required=False)
    password1 =forms.CharField(required=False)
    email= forms.EmailField(required=False)

class approveForm(forms.Form):
    username=forms.CharField(required=True)

class listuserForm(forms.Form):
    select=forms.ChoiceField(choices=ROLE2, required=False)
    
class deleteForm(forms.Form):
    username=forms.CharField(required=True)       

class addmodForm(forms.Form):
    username=forms.CharField(required=False)
    password =forms.CharField(required=False)
    password1 =forms.CharField(required=False)
    email= forms.EmailField(required=False)