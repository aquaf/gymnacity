from django.contrib import admin
from .models import GymServices, GymService, TrainerService, OpeningHours


@admin.register(GymServices)
class GymServicesAdmin(admin.ModelAdmin):
    pass


@admin.register(GymService)
class GymServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(TrainerService)
class TrainerService(admin.ModelAdmin):
    pass


@admin.register(OpeningHours)
class OpeningHours(admin.ModelAdmin):
    pass
