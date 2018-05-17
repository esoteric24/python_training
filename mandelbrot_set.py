import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def initialize_image(xPoints, yPoints):
    image = []
    for i in range(yPoints):
        xColors = []
        for j in range(xPoints):
            xColors.append(0)
        image.append(xColors)
    return image

def color_point(x, y, xPoints, yPoints, maxIter):
    x = -2.5 + (x * (3.5/xPoints))
    y = -1.0 + (y * (2.0/yPoints))
    z1 = 0 + 0j
    c = x + (1j * y)
    iteration = 0
    while True:
        z1 = (z1)**2 + c
        iteration += 1
        if abs(z1) >= 2 or iteration >= maxIter:
            break
    color = iteration
    return color

def plot_points(xPoints, yPoints, maxIter):
    image = initialize_image(xPoints, yPoints)
    for i in range(yPoints):
        for j in range(xPoints):
            image[i][j] = color_point(j, i, xPoints, yPoints, maxIter)
    plt.imshow(image, origin='lower', extent=(-2.5, 1.0, -1.0, 1.0), cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    plt.show()

xPoints = 1000
yPoints = 400
maxIter = 400

plot_points(xPoints, yPoints, maxIter)
