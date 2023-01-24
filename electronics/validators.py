from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_comparison(value):
    if value  > 1:
        raise ValidationError(
            _('%(value)s more than 1, select 0 or 1'),
            params={'value': value},
        )
