from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="is_sudo")
def is_sudo():
    return user.groups.filter(name='sudo')