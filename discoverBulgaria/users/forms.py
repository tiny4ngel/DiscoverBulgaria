from cloudinary.forms import CloudinaryFileField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from discoverBulgaria.users.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    """
        A form for user registration.

        Fields:
            - email: Email address of the user.
            - first_name: First name of the user.
            - last_name: Last name of the user.
            - nationality: Nationality of the user.
            - profile_picture: Profile picture of the user.
            - password1: First password field for user registration.
            - password2: Second password field for user registration.

        Methods:
            - __init__: Initializes the form and sets custom CSS classes for password fields.
            - save: Saves the user registration data and creates a user profile.

        Meta:
            - model: UserModel - the User model.
            - fields: ('email',) - the fields to include in the form.
        """
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
        """
            Save the user registration data and create a user profile.
            Args:
                commit (bool): If True, save the user and profile to the database.
            Returns:
                UserModel: The saved user instance.
        """
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
