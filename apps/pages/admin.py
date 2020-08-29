from django.contrib import admin

from .models import *


@admin.register(Contet)
class ContetAdmin(admin.ModelAdmin):
    pass
