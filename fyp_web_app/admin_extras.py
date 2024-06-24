from django import template

register = template.Library()

@register.simple_tag
def render_image(image_url):
    if image_url:
        return '<img src="{}" style="max-width: 100px; max-height: 100px;">'.format(image_url)
    else:
        return 'No image'
