import random
import matplotlib.pyplot as plt

def transformation1(point):
    x = point[0]
    y = point[1]
    x1 = 0.5*x
    y1 = 0.5*y
    return x1, y1

def transformation2(point):
    x = point[0]
    y = point[1]
    x1 = 0.5*x + 0.5
    y1 = 0.5*y + 0.5
    return x1, y1

def transformation3(point):
    x = point[0]
    y = point[1]
    x1 = 0.5*x + 1
    y1 = 0.5*y
    return x1, y1

def transform(point):
    transformations = [transformation1, transformation2, transformation3]
    transIndex = random.randint(0, 2)
    transFunct = transformations[transIndex]
    x, y = transFunct(point)
    return x, y

def draw_triangle(num):
     x = [0]
     y = [0]
     x1, y1 = 0, 0

     for i in range(num):
         x1, y1 = transform((x1, y1))
         x.append(x1)
         y.append(y1)
     return x, y

num = int(input('Enter the number of points in the triangle: '))
x, y = draw_triangle(num)
plt.plot(x, y, 'o', markersize=1)
plt.title('Triangle with {0} points'.format(num))
plt.show()
