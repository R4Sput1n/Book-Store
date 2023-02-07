from django import template

register = template.Library()


@register.simple_tag
def replace_characters(string, char_a, char_b):
    return string.replace(char_a, char_b)
