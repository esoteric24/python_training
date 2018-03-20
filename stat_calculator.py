def calc_mean(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s/n
    return mean

def calc_median(numbers):
    n = len(numbers)
    numbers.sort()
    if n % 2 == 0:
        m1 = n/2
        m2 = (n/2) + 1
        median = (m1 + m2)/2
    else:
        median = (n + 1)/2
    return median

from collections import Counter

def calc_mode(numbers):
    c = Counter(numbers)
    freqNums = c.most_common()
    maxFreq = freqNums[0][1]
    modes = []
    for num in freqNums:
        if num[1] == maxFreq:
            modes.append(num[0])
    return modes

def calc_variance(numbers):
    def find_diffs (numbers):
        mean = calc_mean(numbers)
        diff = []
        for num in numbers:
            diff.append(num - mean)
        return diff
    diff = find_diffs(numbers)
    squaredDiff = []
    for d in diff:
        squaredDiff.append(d**2)
    variance = sum(squaredDiff)/len(numbers)
    return variance

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers

data = read_data('mydata.txt')
mean = calc_mean(data)
print('Mean: {0}'.format(mean))
median = calc_median(data)
print('Median: {0}'.format(median))
mode = calc_mode(data)
print('Mode(s): {0}'.format(mode))
variance = calc_variance(data)
print('Variance: {0}'.format(variance))
std = variance**0.5
print('Standard deviation: {0}'.format(std))
