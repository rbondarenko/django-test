from django.db import models

class EligibilityRule(models.Model):
    field_to_check = models.CharField(max_length=32, choices=[
        ('product_name', 'Product Name'),
        ('category', 'Category'),
        ('merchant', 'Merchant'),
    ])
    match_text = models.CharField(max_length=128)
    confidence_score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.get_field_to_check_display()}: '{self.match_text}' ({self.confidence_score}%)"

class Submission(models.Model):
    product_name = models.CharField(max_length=128)
    category = models.CharField(max_length=64)
    merchant = models.CharField(max_length=64)
    submitted_at = models.DateTimeField(auto_now_add=True)
    eligible = models.BooleanField(default=False)
    confidence = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        status = 'Eligible' if self.eligible else 'Ineligible'
        return f"{self.product_name} @ {self.merchant} [{status} | {self.confidence}%]"
