#type(), int(), & float()
print(type(3))
print(type(3.5))
print(type(3.0))

print(int(3.8))
print(int(3.0))

print(float(3))

#fractions
from fractions import Fraction
f = Fraction(3, 4)
print(f)

f = Fraction (3, 4) + 1 + 1.5
print(f)

f = Fraction (3, 4) + 1 + Fraction(1, 4)
print(f)

#complex numbers
a = 2 + 3j
print(type(a))

a = complex(2, 3)
print(a)

b = 3 + 3j

print(a + b)
print(a - b)
print(a * b)
print(a / b)

z = 2 + 3j
print(z.real)
print(z.imag)
print(z.conjugate())
print((z.real**2 + z.imag**2)**0.5)
print(abs(z))

#user input
#NONE OF THIS WORKS
#things that do not work as advertised in book:
#inputting "3/4" into int() or float() doesn't raise a ValueError
# it just thinks "3/4" = 0
#inputting a float into int() doesn't raise a ValueError either
# it just rounds the float down
#unable to get .is_integer to work, threw me a NameError??
#the Fraction(input()) thing doesn't work either
# fractions entered in format "numerator/denominator" just equal 0
#so of course I couldn't test the ZeroDivisionError thing either
#this is so frustrating!!
#I blame all of this on you Steve

z = complex(input('Enter a complex number: '))
print(z)

#the above works, but it doesn't throw a ValueError if you put spaces in your complex number
#("3 + 2j" vs "3+2j") like the book says it does
