from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
import datetime

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy'})
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'avatar', 'bio', 'date_of_birth']

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob and (datetime.date.today().year - dob.year) < 13:
            raise ValidationError("Bạn phải từ 13 tuổi trở lên để đăng ký.")
        return dob
