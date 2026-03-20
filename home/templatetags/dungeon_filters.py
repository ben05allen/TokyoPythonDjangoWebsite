from django import template
register = template.Library()

@register.filter
def enumerate(lst):
    return __builtins__['enumerate'](lst)
