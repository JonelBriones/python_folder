# 1
print('1. Countdown')

list = []


def countdown(number):
    for x in range(number, 0, -1):
        list.append(x)
    list.append(0)
    print(list)


(countdown(5))


# 2
print('2. Print and Return')


def printAndReturn(list):
    numbersOfList = list
    print(numbersOfList[0])
    return numbersOfList[1]


print(printAndReturn([1, 2]))
# printAndReturn([1, 2]) why does this not print the return


# 3
print('3. First Plug Length')


def firstPlugLength(list):
    return list[0] + len(list)


print(firstPlugLength([1, 2, 3, 4, 5]))

# 4
print('4. Values Greater than Second')

greaterThanIndexTwo = []


def valueGreaterThanSecond(list):
    for x in (list):

        if len(list) < 2:
            return False

        elif x > list[3]:
            greaterThanIndexTwo.append(x)

    print(len(greaterThanIndexTwo))
    return greaterThanIndexTwo


print(valueGreaterThanSecond([5, 2, 3, 2, 1, 4]))
print(valueGreaterThanSecond([3]))

# 5
print('5. This Length, That Value')


def thisLengthThatValue(a, b):
    newList = []
    newList.append(b)
    return newList * a


print(thisLengthThatValue(4, 7))
print(thisLengthThatValue(6, 2))
