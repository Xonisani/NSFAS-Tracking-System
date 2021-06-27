from django import forms
from .models import Student, StudentLogin
#from passlib.hash import pbkdf2_sha256

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= StudentLogin
        fields= ["student_num", "password", "re_password"]


class UpdateForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= "__all__"


    #def check_if_email_exist(self):
        #email = self.cleaned_data.get('email')
        
        #for instance in Student.objects.all():
            #if instance.email == email:
               # raise forms.ValidationError('The email already exist '+ email)
        #return email