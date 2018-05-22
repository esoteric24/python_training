from sympy import Symbol, Derivative, sympify, solve, pprint
from sympy.core.sympify import SympifyError

# def derive(f, var):
#     var = Symbol(var)
#     fPrime = Derivative(f, var).doit()
#     pprint(fPrime)
#
# function = input('Enter a function: ')
# variable = input('Enter the variable to differentiate with respect to: ')
# try:
#     function = sympify(function)
# except SympifyError:
#     print('Invalid input')
# else:
#     derive(function, variable)

x = Symbol('x')
print(' ')
f = input('Enter the function whose extrema you wish to calculate, in terms of x: ')
xMin = int(input('Enter the left domain boundary of the function: '))
xMax = int(input('Enter the right domain boundary of the function: '))
print(' ')
try:
    f = sympify(f)
except SympifyError:
    print('Invalid input')

fPrime = Derivative(f, x).doit()
critPoints = solve(fPrime)
for index, value in enumerate(critPoints):
    if value < xMin or value > xMax:
        del(critPoints[index])
critPoints.sort()

print('Critical points:')
for point in critPoints:
    print('x = {0}'.format(point))
print(' ')

fTwoPrime = Derivative(f, x, 2).doit()
secondDevVals = []
for point in critPoints:
    val = fTwoPrime.subs({x:point}).evalf()
    secondDevVals.append(val)

print('Second derivative test results:')
slot = 0
while True:
    if slot < len(critPoints):
        print('f\'\'({0}) = {1}'.format(critPoints[slot], secondDevVals[slot]))
        slot += 1
    else:
        break
print(' ')

locMax = []
locMin = []
other = []
for index, value in enumerate(secondDevVals):
    if value > 0:
        locMin.append(critPoints[index])
    elif value < 0:
        locMax.append(critPoints[index])
    else:
        other.append(critPoints[index])

print('Local maxima:')
for point in locMax:
    print('x = {0}'.format(point))
print(' ')
print('Local minima:')
for point in locMin:
    print('x = {0}'.format(point))
print(' ')
if other != []:
    print('Inconclusive:')
    for point in other:
        print('x = {0}'.format(point))
    print(' ')

print('Global extrema test results:')
testPoints = locMax
for point in locMin:
    testPoints.append(point)
for point in other:
    testPoints.append(point)
testPoints.append(xMin)
testPoints.append(xMax)
testOutputs = []
for point in testPoints:
    output = f.subs({x:point}).evalf()
    testOutputs.append(output)
slot = 0
while True:
    if slot < len(testPoints):
        print('f({0}) = {1}'.format(testPoints[slot], testOutputs[slot]))
        slot += 1
    else:
        break
print(' ')

def test_extrema(locEx, other, xMin, xMax, sortOrder):
    globEx = locEx
    for point in other:
        globEx.append(point)
    globEx.append(xMin)
    globEx.append(xMax)
    outputs = []
    for point in globEx:
        output = f.subs({x:point}).evalf()
        outputs.append(output)
    if sortOrder == 'reverse':
        outputOrder = sorted(outputs, reverse=True)
    elif sortOrder == 'forward':
        outputOrder = sorted(outputs)
    result = outputOrder[0]
    for slot, point in enumerate(outputs):
        if point == result:
            exPoint = globEx[slot]
    return exPoint

globalMaximum = test_extrema(locMax, other, xMin, xMax, 'reverse')
globalMinimum = test_extrema(locMin, other, xMin, xMax, 'forward')

print('Global maximum:')
print('x = {0}'.format(globalMaximum))
print(' ')
print('Global minimum:')
print('x = {0}'.format(globalMinimum))
print(' ')
