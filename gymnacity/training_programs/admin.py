from django.contrib import admin
from .models import TrainingProgram


@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    pass
