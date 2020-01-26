from django.contrib import admin
from .models import Muscule


@admin.register(Muscule)
class MusculeAdmin(admin.ModelAdmin):
    pass
