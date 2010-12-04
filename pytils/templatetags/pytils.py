# coding: utf-8
"""
Some of the most useful filters, named to better match Django’s built-ins.
"""

from django import template
from pytils_dt import ru_strftime as ru_date
from pytils_numeral import get_plural as ru_plural
import re

register = template.Library()

def _percent_fmt(f):
    def _f(n, s):
        s = re.sub(r'(?=a|A|b|B|c|d|f|H|I|j|m|M|p|S|U|w|W|x|X|y|Y|z|Z|%)', '%', s)
        return f(n, s)
    return _f

register.filter('ru_date', _percent_fmt(ru_date))
register.filter('ru_plural', ru_plural)
