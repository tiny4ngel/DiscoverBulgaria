from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html

from discoverBulgaria.users.models import Profile, AppUser

CustomUser = get_user_model()


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_staff', 'date_joined', 'favorite_landmarks_link')
    list_filter = ('is_staff', 'date_joined')
    search_fields = ('email', 'profile__first_name', 'profile__last_name')
    readonly_fields = ('get_favorite_landmarks',)

    def full_name(self, obj):
        return obj.get_full_name() if obj.get_full_name() else '-'

    full_name.short_description = 'Full Name'

    def favorite_landmarks_link(self, obj):
        return format_html('<a href="{}">View</a>',
                           reverse('admin:bulgaria_favouritelandmarks_changelist') + f'?traveller__id__exact={obj.id}')

    favorite_landmarks_link.short_description = 'Favorite Landmarks'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'nationality', 'profile_picture_thumbnail')
    list_filter = ('nationality',)
    search_fields = ('user__email', 'first_name', 'last_name')
    readonly_fields = ('profile_picture_thumbnail',)

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = 'Full Name'

    def profile_picture_thumbnail(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50">', obj.profile_picture.url)
        return '-'

    profile_picture_thumbnail.short_description = 'Profile Picture'


admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Profile, ProfileAdmin)