from django.contrib import admin
from .models import DiagnosticReport

@admin.register(DiagnosticReport)
class DiagnosticReportAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'detected_disease', 'confidence_score', 'created_at')
    list_filter = ('is_user_verified',)