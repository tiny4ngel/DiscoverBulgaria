from django import forms
from discoverBulgaria.bulgaria.models import FavouriteLandmarks, Landmarks


class AddToFavouritesForm(forms.ModelForm):
    class Meta:
        model = FavouriteLandmarks
        fields = '__all__'
        widgets = {'landmark': forms.HiddenInput(attrs={'class': 'form-control'}),
                   'traveller': forms.HiddenInput}


class DeleteJoinedLandmark(forms.ModelForm):
    class Meta:
        model = FavouriteLandmarks
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class LandmarksForm(forms.ModelForm):
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
    pass


class DeleteLandmark(forms.ModelForm):
    class Meta:
        model = Landmarks
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
