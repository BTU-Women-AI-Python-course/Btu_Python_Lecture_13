from django.core.exceptions import ValidationError


def validate_age(value):
    if value < 18:
        raise ValidationError(
            "თქვენ არ ხართ სრულწლოვანი",
            params={"value": value},
        )
