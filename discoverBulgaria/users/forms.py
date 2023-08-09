from cloudinary.forms import CloudinaryFileField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from discoverBulgaria.users.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    NATIONALITY_CHOICES = [
        ('BG', 'Bulgarian'),
        ('EN', 'English'),
        ('TR', 'Turkish'),
        ('FR', 'French'),
        ('ES', 'Spanish'),
        ('RU', 'Russian'),
        ('OT', 'Other'),
    ]
    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    field_order = ('email', 'first_name', 'last_name', 'password1', 'password2', 'nationality', 'profile_picture')

    class Meta:
        model = UserModel
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile_picture = self.cleaned_data.get('profile_picture', None)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            nationality=self.cleaned_data['nationality'],
            profile_picture=profile_picture,
            user=user,
        )
        if commit:
            profile.save()

        return user


