from django import forms
from discoverBulgaria.bulgaria.models import FavouriteLandmarks, Landmarks


class AddToFavouritesForm(forms.ModelForm):
    """
        A form to add a landmark to favorites.
        Meta:
            model: FavouriteLandmarks - the FavouriteLandmarks model.
            fields: '__all__' - all fields of the model.
            widgets: Custom widgets for the form fields.
    """

    class Meta:
        model = FavouriteLandmarks
        fields = '__all__'
        widgets = {'landmark': forms.HiddenInput(attrs={'class': 'form-control'}),
                   'traveller': forms.HiddenInput}


class DeleteJoinedLandmark(forms.ModelForm):
    """
        A form to delete a landmark from favorites.
        Meta:
            model: FavouriteLandmarks - the FavouriteLandmarks model.
            fields: () - no fields included in the form.
        Methods:
            save: Deletes the instance from the database if commit is True.
        Returns:
            FavouriteLandmarks: The instance being deleted.
    """

    class Meta:
        model = FavouriteLandmarks
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class LandmarksForm(forms.ModelForm):
    """
        A form for adding or editing a landmark.
        Meta:
            model: Landmarks - the Landmarks model.
            fields: '__all__' - all fields of the model.
            widgets: Custom widgets for the form fields.
    """

    class Meta:
        model = Landmarks
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'landmark_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'trip_time': forms.TextInput(attrs={'class': 'form-control'}),
            'historic_context': forms.Textarea(attrs={'class': 'form-control'}),
            'architectural_features': forms.Textarea(attrs={'class': 'form-control'}),
            'visitor_information': forms.Textarea(attrs={'class': 'form-control'}),
            'accessibility': forms.Textarea(attrs={'class': 'form-control'}),
            'additional_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'cover_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class LandmarksEditForm(LandmarksForm):
    """
        A form for editing a landmark, inheriting from LandmarksForm.
    """
    pass


class DeleteLandmark(forms.ModelForm):
    """
        A form for deleting a landmark.
        Meta:
            model: Landmarks - the Landmarks model.
            fields: () - no fields included in the form.
        Methods:
            save: Deletes the instance from the database if commit is True.
        Returns:
            Landmarks: The instance being deleted.
    """

    class Meta:
        model = Landmarks
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
