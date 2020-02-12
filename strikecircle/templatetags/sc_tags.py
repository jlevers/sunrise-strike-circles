from django import template

register = template.Library()

@register.filter
def index(value, arg):
    try:
        val = value[arg]
    except (IndexError, KeyError):
        val = None

    return val

@register.filter
def addstr(value, arg):
    return f'{value}{arg}'
