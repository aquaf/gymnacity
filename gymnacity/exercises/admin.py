from django.contrib import admin
from .models import Exercise, ExerciseDetail


@admin.register(Exercise)
class ExercisemanAdmin(admin.ModelAdmin):
    pass


@admin.register(ExerciseDetail)
class ExerciseDetailmanAdmin(admin.ModelAdmin):
    pass
