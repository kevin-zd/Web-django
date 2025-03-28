from django import template

register = template.Library()

@register.filter("toFixed")
def filter_to_fixed(content, len=2):
    return f"{content:.2f}"