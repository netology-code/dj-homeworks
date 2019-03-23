from django.template import Library


def repalce_dot_to_comma(number):
    try:
        float(number)
        number = number.replace('.', ',')
    except ValueError:
        pass
    return number

register = Library()
register.filter(name='repalce_dot_to_comma', filter_func=repalce_dot_to_comma)
