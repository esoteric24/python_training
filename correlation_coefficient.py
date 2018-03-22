def find_correl(x,y):
    n = len(x)

    prodsXY = []
    for xn,yn in zip(x,y):
        prodsXY.append(xn*yn)

    sumProdsXY = sum(prodsXY)
    sumX = sum(x)
    sumY = sum(y)
    squaredSumX = sumX**2
    squaredSumY = sumY**2

    xSquared = []
    for xn in x:
        xSquared.append(xn**2)
    xSquaredSum = sum(xSquared)

    ySquared = []
    for yn in y:
        ySquared.append(yn**2)
    ySquaredSum = sum(ySquared)

    numerator = (n*sumProdsXY) - (sumX*sumY)
    denomTerm1 = (n*xSquaredSum) - (squaredSumX)
    denomTerm2 = (n*ySquaredSum) - (squaredSumY)
    denominator = (denomTerm1*denomTerm2)**0.5
    correlation = numerator/denominator

    return correlation


x = []
while True:
    answer = raw_input('Enter a value in the first set of data, or type "done" if you have completed the first set: ')
    print
    if answer == 'done':
        break
    else:
        x.append(int(answer))

y = []
while True:
    answer = raw_input('Enter a value in the second set of data, or type "done" if you have completed the second set: ')
    print
    if answer == 'done':
        break
    else:
        y.append(int(answer))

correlation = find_correl(x,y)
print('Correlation: {0}'.format(correlation))
print
