from django import template
from xwcs.base.models import H5PModule

register = template.Library()

@register.inclusion_tag('h5p_module_template.html', takes_context=True)
def h5p_module(context):

    print(context['block'].value.h5p_file)
    return {
        'h5p_modules': None,
        # 'h5p_module': H5PModule.objects.all(),
        'context': context,
        'request': context['request'],
        'test_text': "hello"
    }