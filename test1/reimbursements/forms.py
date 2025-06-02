from django import forms
from .models import Submission, EligibilityRule
from .services import EligibilityEvaluator


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['product_name', 'category', 'merchant']

    def save(self, commit=True):
        instance = super().save(commit=False)

        evaluator = EligibilityEvaluator()
        is_eligible, confidence_score = evaluator.evaluate(instance.product_name, instance.category, instance.merchant)
        instance.eligible = is_eligible
        instance.confidence = confidence_score

        if commit:
            instance.save()
        return instance


