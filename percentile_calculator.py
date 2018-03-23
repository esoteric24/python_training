def calc_percentile(data,p):
    data.sort()
    n = len(data)
    i = (n*p)/100 + 0.5
    def check_int(i,data):
        i = float(i)
        if i.is_integer() == True:
            i = int(i)
            output = data[i]
            return output
        else:
            k = int(i)
            f = i - k
            term1 = (1-f)*data[k]
            term2 = f*data[k+1]
            output = term1 + term2
            return output
    output = check_int(i,data)
    return output

data = [5, 1, 9, 3, 14, 9, 7]
p = int(raw_input('Enter the percentile you wish to calculate: '))
answer = calc_percentile(data,p)
print('{0} is the number corresponding to percentile {1}'.format(answer,p))
