from django import forms
from register.models import CustomUser


class UserCreationForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name','email','age','image','password']
        widgets={"password":forms.PasswordInput()}

    def save(self,commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user