# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter
def get_item(value, arg=''):
    result = ''
    if isinstance(value, dict):
        result = value.get(arg, '')
    return result
