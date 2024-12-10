from django import template

register = template.Library()


@register.simple_tag()
def menu_tag():
    return [
        {'title': 'About', 'url': 'about'},
        {'title': 'Shop', 'url': 'shop'},
        {'title': 'Contacts', 'url': 'contacts'},
    ]
