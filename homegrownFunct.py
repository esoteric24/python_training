def check_int(a):
    try:
        a = float(a)
        if a.is_integer() == True:
            a = int(a)
            print('%s is a valid integer' % a)
        else:
            print('You entered an invalid integer')
    except ValueError:
        try:
            a = int(a)
            print('%s is a valid integer' % a)
        except ValueError:
            print('You entered an invalid integer')

def check_fraction(a):
    from fractions import Fraction
    try:
        a = Fraction(a)
        print(a)
    except ValueError:
        print('You entered an invalid fraction')
    except ZeroDivisionError:
        print('You entered an invalid fraction')

def check_complex(z):
    try:
        z = complex(z)
        print(z)
    except ValueError:
        z = z.replace(' ', '')
        z = z.replace('i', 'j')
        try:
            z = complex(z)
            print(z)
        except ValueError:
            print('You entered an invalid complex number')

def is_factor(a, b):
    if b % a == 0:
        global value
        value = True
        return value
    else:
        value = False
        return value
