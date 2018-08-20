from django import template


register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    return value


# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    # Ваш код
    return value



