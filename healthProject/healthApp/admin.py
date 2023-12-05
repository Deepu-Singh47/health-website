from django.contrib import admin
from .models import patient, symptom, treatment

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'contact', 'email')

class TreatmentAdmin(admin.ModelAdmin):
    list_display=('symptom','possible_diseases','treatment')

admin.site.register(patient, UserAdmin)
admin.site.register(symptom)
admin.site.register(treatment, TreatmentAdmin)
