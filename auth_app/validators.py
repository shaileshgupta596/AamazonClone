from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def is_email_present(email):
    try:
        get_object_or_404(User, username=email)
    except:
        raise ValidationError('Email Does Not Exists.')


def is_account_active(email):
    try:
        user = get_object_or_404(User, username=email)
        if not user.is_active:
            raise ValidationError("Account is not active.")
    except:
        raise ValidationError('Email Does Not Exists.')