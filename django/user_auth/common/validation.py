import re


def passwordValidate(password):
    if len(password) < 8:
        return False
    elif re.search('[0-9]+', password) is None:
        return False
    elif re.search('[a-zA-Z]+', password) is None:
        return False
    elif re.search('[`~!@#$%^&*(),<.>/?]+', password) is None:
        return False
    else:
        return True


def emailValidate(email):
    p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if p.match(email) is None:
        return False
    else:
        return True