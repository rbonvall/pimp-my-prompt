#!/usr/bin/python

from os import environ

def cyan(x):
    return x

def host_name():
    return r'\h'
def current_directory():
    return r'\w'
def user():
    return r'\u'

prompts = dict()

prompt_symbol = cyan('$ ')
separator = cyan(':')

prompts['minimal'] = prompt_symbol
prompts['classical'] = (user() + '@' + host_name() + separator +
                        current_directory() + prompt_symbol)
prompts['simple'] = (current_directory() + prompt_symbol)


if __name__ == '__main__':
    from sys import argv
    if len(argv) == 1:
        for p in sorted(prompts):
            print p
    elif len(argv) == 2 and argv[1] in prompts:
        print 'export PS1="{}"'.format(prompts[argv[1]])
    else:
        print 'Usage: %s [prompt_name]' % argv[0]

