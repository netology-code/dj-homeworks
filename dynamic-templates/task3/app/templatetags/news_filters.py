from django import template
import time
import datetime


register = template.Library()

def create_word_form(value, form1, form2, form3):
    if value // 10 % 10 == 1:
        return form3
    if value % 10 == 1:
        return form1
    if value % 10 in [2, 3, 4]:
        return form2
    return form3

@register.filter
def format_date(value):
    # Ваш код

    value = int(value)
    delta = time.time() - value

    if delta < 10 * 60:
        return 'только что'
    if delta < 24 * 60 * 60:
        hours = int(delta / 60 / 60)
        return f'{hours} {create_word_form(hours, "час", "часа", "часов")} назад'
    return datetime.datetime.fromtimestamp(value).strftime('%Y-%m-%d')

# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):
    value = int(value)
    if value > 5:
        return 'хороший'
    if value < -5:
        return 'плохой'
    return 'нейтральный'

# необходимо добавить фильтр для поля `score`
@register.filter
def color_score(value):
    value = int(value)
    if value > 5:
        return 'green'
    if value < -5:
        return 'lime'
    return 'orange'

@register.filter
def format_num_comments(value):
    # Ваш код
    value = int(value)
    if value == 0:
        return 'Оставьте комментарий'
    if value < 50:
        word = create_word_form(value, "комментарий", "комментария", "комментариев")
        return f'{value} {word}'
    return 'Больше 50 комментариев'

@register.filter
def format_selftext(value, arg):
    value = value.split(' ')
    arg = int(arg)
    if len(value) < int(arg * 2):
        return ' '.join(value)
    return ' '.join([*value[:arg], '...', *value[-arg:]])


