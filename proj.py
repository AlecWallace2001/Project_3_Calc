def addNum(numA, numB, numC):
    sums = int(numA)+int(numB)+int(numC)
    if len(str(sums)) == 1:
        return str(sums), '0', 0
    else:
        return str(sums)[1], str(sums)[0], 1


def mainAdd(numA, numB):
    numA = numA[::-1]
    numB = numB[::-1]
    Tens = '0'
    mSum = []
    if len(numA) > len(numB):
        for i in range(len(numA)):
            try:
                rSum, Tens, xApp = addNum(numA[i], numB[i], Tens)
                mSum.append(rSum)
            except:
                rSum, Tens, xApp = addNum(numA[i], '0', Tens)
                mSum.append(rSum)
    elif len(numB)> len(numA):
        for i in range(len(numB)):
            try:
                rSum, Tens, xApp = addNum(numA[i], numB[i], Tens)
                mSum.append(rSum)
            except:
                rSum, Tens, xApp = addNum('0', numB[i], Tens)
                mSum.append(rSum)
    else:
        for i in range(len(numB)):
            rSum, Tens, xApp = addNum(numA[i], numB[i], Tens)
            mSum.append(rSum)
    if xApp == 1:
        mSum.append(Tens)
    sSum = mSum[::-1]
    fSum = ''
    for i in sSum:
        fSum = fSum + i
    return fSum

def mainMult(multA, multB):
    multH = multA
    
    for i in range(int(multB)-1):
        multH = mainAdd(multH, multA)
    
    return multH

def MainExp(expA, expB):
    expH = expA
    for i in range(int(expB)-1):
        expH = mainMult(expH, expA)
    return expH
    

print "1.) addition"
print "2.) multiplication"
print "3.) exponent"
function = raw_input("Which Function? ")
mainNum = raw_input("Enter the first number: ")
subNum = raw_input("Enter the second number: ")
if function == '1':
    tSum = mainAdd(mainNum, subNum)
    print tSum
elif function == '2':
    tProd = mainMult(mainNum, subNum)
    print tProd
elif function == '3':
    tExp = MainExp(mainNum, subNum)
    print tExp

