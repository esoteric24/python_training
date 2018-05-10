import random
import matplotlib.pyplot as plt

def transformation1(point):
    x = point[0]
    y = point[1]
    x1 = 0.85*x + 0.04*y
    y1 = -0.04*x + 0.85*y + 1.6
    return x1, y1

def transformation2(point):
    x = point[0]
    y = point[1]
    x1 = 0.2*x - 0.26*y
    y1 = 0.23*x + 0.22*y + 1.6
    return x1, y1

def transformation3(point):
    x = point[0]
    y = point[1]
    x1 = -0.15*x + 0.28*y
    y1 = 0.26*x + 0.24*y + 0.44
    return x1, y1

def transformation4(point):
    x = point[0]
    y = point[1]
    x1 = 0
    y1 = 0.16*y
    return x1, y1

def get_index():
    r = random.random()
    sumProb = [0.85, 0.92, 0.99, 1.0]
    for index, value in enumerate(sumProb):
        if r <= value:
            return index
    return len(probability)-1

def transform(point):
    transformations = [transformation1, transformation2, transformation3, transformation4]
    transIndex = get_index()
    transFunct = transformations[transIndex]
    x, y = transFunct(point)
    return x, y

def draw_fern(num):
     x = [0]
     y = [0]
     x1, y1 = 0, 0
     for i in range(num):
         x1, y1 = transform((x1, y1))
         x.append(x1)
         y.append(y1)
     return x, y

num = int(input('Enter the number of points in the fern: '))
x, y = draw_fern(num)
plt.plot(x, y, 'go', markersize=0.01)
plt.title('Fern with {0} points'.format(num))
plt.show()
