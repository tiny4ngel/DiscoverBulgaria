from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from discoverBulgaria.bulgaria.models import Landmarks, FavouriteLandmarks, HistoricFigure, QuizQuestion, Choice, \
    Leaderboard


class LandmarksAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'trip_time')
    list_filter = ('title',)
    search_fields = ('title', 'location')


class FavouriteLandmarksAdmin(admin.ModelAdmin):
    list_display = ('traveller_full_name', 'get_favorite_landmarks')

    def traveller_full_name(self, obj):
        return obj.traveller.get_full_name()

    traveller_full_name.short_description = 'Traveler'

    def get_favorite_landmarks(self, obj):
        return obj.traveller.get_favorite_landmarks()

    get_favorite_landmarks.short_description = 'Favorite Landmarks'


class HistoricFigureAdmin(admin.ModelAdmin):
    list_display = ('name', 'lifespan', 'unlocked_by_list')
    list_filter = ('lifespan', 'unlocked_by',)
    search_fields = ('name', 'lifespan')
    ordering = ('name',)

    def unlocked_by_list(self, obj):
        return ', '.join([user.email for user in obj.unlocked_by.all()])

    unlocked_by_list.short_description = 'Unlocked By'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('formatted_historic_figure', 'question_text')
    search_fields = ('question_text', 'historic_figure__name')
    ordering = ('historic_figure__name', 'id')

    def formatted_historic_figure(self, obj):
        return format_html("<strong>{}</strong>", obj.historic_figure.name)

    formatted_historic_figure.short_description = 'Historic Figure'


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('historic_figure', 'question', 'choice_text', 'is_correct')
    list_filter = ('question__historic_figure',)
    search_fields = ('choice_text', 'question__question_text')
    list_editable = ('is_correct',)
    list_per_page = Choice.objects.count()

    def historic_figure(self, obj):
        return obj.question.historic_figure

    historic_figure.short_description = 'Historic Figure'


class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user_full_name', 'points')
    list_filter = ('points',)
    search_fields = ('user__profile__first_name', 'user__profile__last_name')  # Update the search fields
    ordering = ('-points',)

    def user_full_name(self, obj):
        return f"{obj.user.profile.first_name} {obj.user.profile.last_name}"
    user_full_name.short_description = 'User Full Name'


admin.site.register(Landmarks, LandmarksAdmin)
admin.site.register(FavouriteLandmarks, FavouriteLandmarksAdmin)
admin.site.register(HistoricFigure, HistoricFigureAdmin)
admin.site.register(QuizQuestion, QuizQuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Leaderboard, LeaderboardAdmin)

