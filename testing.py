from fractions import Fraction

# #type(), int(), & float()
# print(type(3))
# print(type(3.5))
# print(type(3.0))
#
# print(int(3.8))
# print(int(3.0))
#
# print(float(3))
#
# #fractions
# f = Fraction(3, 4)
# print(f)
#
# f = Fraction (3, 4) + 1 + 1.5
# print(f)
#
# f = Fraction (3, 4) + 1 + Fraction(1, 4)
# print(f)
#
# #complex numbers
# a = 2 + 3j
# print(type(a))
#
# a = complex(2, 3)
# print(a)
#
# b = 3 + 3j
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
#
# z = 2 + 3j
# print(z.real)
# print(z.imag)
# print(z.conjugate())
# print((z.real**2 + z.imag**2)**0.5)
# print(abs(z))

#user input

# try:
#     a = float(input('Enter a number: '))
# except ValueError:
#     print('You entered an invalid number')

# def check_int(a):
#     try:
#         a = float(a)
#         if a.is_integer() == True:
#             a = int(a)
#             print('%s is a valid integer' % a)
#         else:
#             print('You entered an invalid integer')
#     except ValueError:
#         try:
#             a = int(a)
#             print('%s is a valid integer' % a)
#         except ValueError:
#             print('You entered an invalid integer')
#
# a = check_int(input('Please enter an integer: '))


def check_Fraction(a):
    from fractions import Fraction
    try:
        a = Fraction(a)
        print(a)
    except ValueError:
        print('You entered an invalid fraction')
    except ZeroDivisionError:
        print('You entered an invalid fraction')

a = check_Fraction(input('Enter a fraction: '))

# z = input('Enter a complex number: ')
#
# try:
#     z = complex(z)
#     print(z)
# except ValueError:
#     z = z.replace(' ', '')
#     z = z.replace('i', 'j')
#     try:
#         z = complex(z)
#         print(z)
#     except ValueError:
#         print('You entered an invalid complex number')
#
# def is_factor(a, b):
#     if b % a == 0:
#         return True
#     else:
#         return False
