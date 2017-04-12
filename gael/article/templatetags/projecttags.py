from django import template
from django.utils.safestring import mark_safe
register = template.Library()
import datetime
@register.filter
def date_change(data, to_format):
    creation_date = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%SZ').strftime(to_format)
    return mark_safe(creation_date)