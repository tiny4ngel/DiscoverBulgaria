from django import forms

from discoverBulgaria.bulgaria.models import FavouriteLandmarks


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
