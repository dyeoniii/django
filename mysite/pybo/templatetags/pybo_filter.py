import markdown
from django import template
from django.utils.safestring import mark_safe

register=template.Library() #필터나 함수를 실제로 등록해주기위한 객체화하는것

@register.filter #실제등록
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    extensions=["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))