# coding: utf-8
"""
Some of the most useful filters, named to better match Django’s built-ins.
"""

from django import template
from pytils_dt import ru_strftime as ru_date
from pytils_numeral import get_plural as ru_plural

register = template.Library()

register.filter('ru_date', ru_date)
register.filter('ru_plural', ru_plural)
