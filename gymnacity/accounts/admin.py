from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Sportsman, Trainer, Gym


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', ]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('О пользователе'), {
            'fields': (
                'user_type',
                'city',)
            }),
        (('Статус пользователя'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',)
            }),
        (('Даты'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'city', 'password1', 'password2')
        }),
    )


@admin.register(Sportsman)
class SportsmanAdmin(admin.ModelAdmin):
    pass

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    pass


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    pass
