import random

def roll(number, value):
    rolls = []
    for each in range (number):
        result = random.randint(1, value)
        rolls.append(result)
    return rolls

def extract_mod(userString):
    posMod = userString.find(' + ')
    negMod = userString.find(' - ')
    if posMod > -1:
        modifier = int(userString[(posMod + 3):])
        userString = userString[:posMod]
    elif negMod > -1:
        modifier = (int(userString[(negMod + 3):]))*-1
        userString = userString[:negMod]
    return userString, modifier

def find_num_val_mod(userString):
    modifierLoc = userString.find(' ')
    modifier = 0
    if modifierLoc != -1:
        outputs = extract_mod(userString)
        userString = outputs[0]
        modifier = outputs[1]
    dPos = userString.find('d')
    if userString[:dPos] != '':
        number = int(userString[:dPos])
    else:
        number = 1
    value = int(userString[(dPos + 1):])
    return number, value, modifier

while True:
    userString = input('Roll ')
    strings = []

    while True:
        commaLoc = userString.find(',')
        if commaLoc != -1:
            subString = userString[:commaLoc]
            strings.append(subString)
            userString = userString[(commaLoc + 2):]
        else:
            strings.append(userString)
            break

    results = []
    sums = []

    for x in strings:
        outputs = find_num_val_mod(x)
        number = outputs[0]
        value = outputs[1]
        modifier = outputs[2]
        result = roll(number, value)
        resultSum = sum(result) + modifier
        results.append(result)
        sums.append(resultSum)

    if value == 20 and number == 2:
        result = results[0]
        advAnswer = input('Is this roll at advantage or disadvantage? Type "adv" or "disadv": ')
        sortResult = sorted(result)
        print('Dice rolls: {0}'.format(result))
        if advAnswer == 'adv':
            total = sortResult[1] + modifier
            print('Total: {0}'.format(total))
        elif advAnswer == 'disadv':
            total = sortResult[0] + modifier
            print('Total: {0}'.format(total))
        else:
            total = sums[0]
            print('Total: {0}'.format(total))
    else:
        if len(results) == 1:
            result = results[0]
            print('Dice rolls: {0}'.format(result))
        else:
            print('Dice rolls: {0}'.format(results))
        total = sum(sums)
        print('Total: {0}'.format(total))

    print(' ')
    escape = input('Do you wish to exit the program? Type "yes" or "no": ')
    print(' ')
    if escape == 'yes':
        break
