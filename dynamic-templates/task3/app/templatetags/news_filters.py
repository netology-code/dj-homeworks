from django import template
import datetime
import time
import re

register = template.Library()


@register.filter
def format_date(value):
    dtnow = time.localtime()
    deltadt = time.mktime(dtnow) - value
    hours = time.strftime("%H", time.gmtime(deltadt))
    if deltadt < 600:
        return 'только что'
    elif deltadt < 86400:
        return hours + ' ' + 'часов назад'
    else:
        return datetime.datetime.fromtimestamp(value).strftime('%d.%m.%Y')


# необходимо добавить фильтр для поля `score`
@register.filter
def score(value: int, default: str):
    if value <= -5:
        return 'все плохо'
    elif -5 < value <= 5:
        return 'нейтрально'
    elif value > 5:
        return 'хорошо'
    else:
        return default


@register.filter
def format_num_comments(value: int):
    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value <= 50:
        return value
    else:
        return '50+'


@register.filter
def format_selftext(value: str, count: int):
    word_first = re.findall(r'\w+\S+', value)[:count]
    word_last = re.findall(r'\w+\S+', value)[-count:]
    text_first = ' '.join(map(str, word_first))
    text_last = ' '.join(map(str, word_last))
    if text_first:
        return text_first + '...' + text_last
    else:
        return '__________________________________________________________'
