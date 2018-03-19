import matplotlib.pyplot as plt

def createBarChart(values, catLabels, xLabel, yLabel, title):
    numBars = len(values)
    barCenters = range(1, (numBars + 1))
    plt.barh(barCenters, values, align='center')
    plt.yticks(barCenters, catLabels)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid()
    plt.show()

values = []
catLabels = []

title = raw_input('Enter the title of the graph: ')
print
xLabel = raw_input('Enter the x-axis label of the graph: ')
print
yLabel = raw_input('Enter the y-axis label of the graph: ')
print
numBars = int(raw_input('Enter the number of the bars in the graph: '))
print
for filler in range(numBars):
    catLabels.append(raw_input('Enter the label of the bar: '))
    print
    values.append(int(raw_input('Enter the value of the bar: ')))
    print

createBarChart(values, catLabels, xLabel, yLabel, title)
