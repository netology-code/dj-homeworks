from django import template


register = template.Library()

@register.filter('getattribute')
def getattribute(value, atr):
    try:
        return value.__getattribute__(atr)
    except AttributeError:
        return value