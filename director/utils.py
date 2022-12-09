from django.forms import ValidationError


def validate_phone_number(phone: str):
    phone = phone.replace(' ', '')
    if len(phone) != 12:
        raise ValidationError('this number error')
    if not phone.startswith('+7'):
        raise ValidationError('Invalid phone number')
    numbers = '+0987654321'
    for i in phone:
        if i not in numbers:
            raise ValidationError(f'number error "{i}"')

