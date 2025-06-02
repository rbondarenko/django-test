from typing import Tuple, List
from .models import EligibilityRule


class EligibilityEvaluator:
    def __init__(self):
        self.rules = list(EligibilityRule.objects.all())

    def evaluate(self, product_name: str, category: str, merchant: str) -> Tuple[bool, int]:
        matched_confidences: List[int] = []

        for rule in self.rules:
            field_val = {'product_name': product_name, 'category': category, 'merchant': merchant}.get(rule.field_to_check, '')
            if rule.match_text.lower() in field_val.lower():
                matched_confidences.append(rule.confidence_score)

        if matched_confidences:
            return True, max(matched_confidences)
        else:
            return False, 0
