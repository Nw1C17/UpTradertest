from django import template

from menu_app.models import MenuItem


from django.template.loader import render_to_string


register = template.Library()

@register.simple_tag
def draw_menu(name):
    template = '{template_name}.html'.format(template_name='base')
    menu_items = MenuItem.objects.filter(name = name).prefetch_related('children')
    context = {'menu_items': menu_items, }
    return render_to_string(template, context)

