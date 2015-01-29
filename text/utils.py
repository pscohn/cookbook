import re

def print_dict(d):
    for k, v in d.items():
        print('%s: %s' % (k, v))

def quote(st):
    return "'" + st + "'"

def comma_separated(fields):
    return ', '.join(fields)

def camel_to_underscores(name):
    split = re.split('([A-Z])', name)
    result = ''
    for s in split:
        if s != '':
            if len(s) == 1 and s.isupper():
                result += '_' + s.lower()
            elif len(s) > 1 and s.islower():
                result += s
    result = result.strip('_')
    return result
