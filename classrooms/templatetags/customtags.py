from django import template

register = template.Library()

@register.simple_tag
def get_classes_by_level(school_year, level):
    return school_year.classrooms.filter(level=level)
