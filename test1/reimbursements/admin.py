from django.contrib import admin
from .models import EligibilityRule, Submission

@admin.register(EligibilityRule)
class EligibilityRuleAdmin(admin.ModelAdmin):
    list_display = ('field_to_check', 'match_text', 'confidence_score')
    list_filter = ('field_to_check',)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'merchant', 'eligible', 'confidence', 'submitted_at')
    list_filter = ('eligible',)
