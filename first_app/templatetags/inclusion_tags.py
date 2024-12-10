from django import template

register = template.Library()


@register.inclusion_tag(filename='first_app/inclusion_html.html')
def include_part_of_html():
    return {
        'some_string': 'string',
        'some_number': 123,
        'some_list': [1, 2, 3],
    }
