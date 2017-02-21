# wrapping 101
def add_wrap(item):
    def wrap_item():
        return 'box for {}'.format(str(item()))
    return wrap_item

@add_wrap
def foo():
    return 'im foo'

@add_wrap
@add_wrap
def moo():
    return 'im moo'

print(foo(),'\n',moo())

from functools import wraps

def style_wrap(addstyle):
    def add_wrap(func_item):
        return '{} box for {}'.format(addstyle,func_item())
    return add_wrap

@style_wrap(' big ')
def goo():
    return 'im goo'

print(goo)
