from django import template

register = template.Library()

@register.filter(name='my_cut')
def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string
    """
    return value.replace(arg,'')

#Can register filter by a separate call or via a decorator
#can use decorators whenever passing a function into another function (composition)
#register.filter('my_cut', cut)
