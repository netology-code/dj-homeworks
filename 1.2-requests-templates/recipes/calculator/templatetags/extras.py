from django import template

register = template.Library()


@register.simple_tag()
def multiply(x, y):
    z = x * y
    if type(x) == int:
        return round(z)
    else:
        return round(z, 2)
