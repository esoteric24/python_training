print(' ')
trait1 = input('Enter the first trait: ')
trait2 = input('Enter the second trait: ')
domMark = input('You have entered "{0}" and "{1}" as your two traits. Of the two, which is dominant? Press 1 for {0} and 2 for {1}: '.format(trait1, trait2))
if domMark == '1':
    trait1 = trait1.capitalize()
    dom = trait1
    rec = trait2
    domVar = dom[0]
    recVar = domVar.lower()
elif domMark == '2':
    trait2 = trait2.capitalize()
    dom = trait2
    rec = trait1
    domVar = dom[0]
    recVar = domVar.lower()
else:
    print('Invalid input')
print(' ')
domPop = float(input('Enter the number of organisms with the {0} trait in the population: '.format(dom)))
recPop = float(input('Enter the number of organisms with the {0} trait in the population: '.format(rec)))
print(' ')
totalPop = domPop + recPop
domPerc = (100*domPop)/totalPop
recPerc = (100*recPop)/totalPop
recFreq = (recPerc/100)**0.5
domFreq = 1 - recFreq
domPrintFreq = domFreq*100
recPrintFreq = recFreq*100
print('Where {0} represents the {1} trait and {2} represents the {3} trait:'.format(domVar, dom, recVar, rec))
print('Percent frequency of {0} allele: {1:.0f}%'.format(domVar, domPrintFreq))
print('Percent frequency of {0} allele: {1:.0f}%'.format(recVar, recPrintFreq))
print(' ')
ddPop = recPop
DDPop = (domFreq**2)*totalPop
DdPop = totalPop - ddPop - DDPop
print('Number of individuals in population with alleles {0}{1}: {2:.0f}'.format(domVar, domVar, DDPop))
print('Number of individuals in population with alleles {0}{1}: {2:.0f}'.format(domVar, recVar, DdPop))
print('Number of individuals in population with alleles {0}{1}: {2:.0f}'.format(recVar, recVar, ddPop))
print(' ')
