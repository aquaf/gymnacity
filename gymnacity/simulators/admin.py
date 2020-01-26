from django.contrib import admin
from .models import Simulator


@admin.register(Simulator)
class SimulatorAdmin(admin.ModelAdmin):
    pass
