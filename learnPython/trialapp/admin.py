from django.contrib import admin
from trialapp.models import trialapp

# Register your models here.
class AppAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(trialapp, AppAdmin)
