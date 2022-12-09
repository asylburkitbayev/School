from django.forms import ValidationError


def validate_phone_number(phone: str):
    phone = phone.replace(' ', '')
    if len(phone) != 12:
        raise ValidationError('Номер телефона не может быть меньше 12 символов.')
    if not phone.startswith('+7'):
        raise ValidationError('Пишите номер в международном формате.')
    numbers = '+0987654321'
    for i in phone:
        if i not in numbers:
            raise ValidationError(f'Телефонный номер не может содержать "{i}"!')