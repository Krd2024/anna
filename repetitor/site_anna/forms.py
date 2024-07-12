from .models import Review, User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("text", "rating")


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False  # Делает аккаунт неактивным до подтверждения email
        if commit:
            user.save()
        return user
