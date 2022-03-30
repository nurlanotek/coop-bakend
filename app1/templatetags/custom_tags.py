from django import template
from django.urls import reverse
from django.contrib.auth.models import Group

register = template.Library()

@register.simple_tag
def anchor(url_name, section_id):
    return reverse(url_name) + '#' + section_id

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False