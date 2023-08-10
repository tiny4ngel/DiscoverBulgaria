from django.contrib import admin

from discoverBulgaria.bulgaria.models import Landmarks, FavouriteLandmarks, HistoricFigure, QuizQuestion, Choice

# Register your models here.
admin.site.register(Landmarks)
admin.site.register(FavouriteLandmarks)
admin.site.register(HistoricFigure)
admin.site.register(QuizQuestion)
admin.site.register(Choice)
