from django import template

register = template.Library()

@register.simple_tag
def get_classes_by_level(school, level):
    return school.classrooms.filter(level=level)
