from django import template
import re


register = template.Library()

BADWORDS = ['using', 'major', 'interval', 'perfect', 'AAAAA']


@register.filter
def wordsfilter(value):
    result = value
    for word in BADWORDS:
        result = re.sub(word, '*' * len(word), result, flags=re.IGNORECASE)
    return result
