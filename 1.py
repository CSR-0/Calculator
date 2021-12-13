def divide(str):
    arry = []
    loopCounter = 0
    if len(str) % 2 == 1:
        str += '_'
    while loopCounter < len(str):
        arry.append(str[loopCounter] + str[loopCounter + 1])
        loopCounter += 2
    return arry

a = divide('Cesar')

print(a)
