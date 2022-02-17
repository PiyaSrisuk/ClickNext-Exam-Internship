# 1 match plus number
def matchNum(arr, sum):
    for idi, i in enumerate(arr):
        for idj, j in enumerate(arr):
            if i + j == sum and idi != idj:
                print(i, j)
                arr.pop(idi)
                arr.pop(idj)


# matchNum([1, 2, 3, 4, 5], 5)
# matchNum([1, 2, 3, 4, 5], 4)

# 2 check similar word
def matchWords(s1, s2):
    if len(s1) != len(s2): return False
    imatch = []
    jmatch = []

    for idi, i in enumerate(s1):
        for idj, j in enumerate(s2):
            asciii = ord(i)
            asciij = ord(j)
            if asciii > 96 and asciii < 123:
                asciii -= 32
            if asciij > 96 and asciij < 123:
                asciij -= 32
            if asciii == asciij and idi not in imatch and idj not in jmatch:
                imatch.append(idi)
                jmatch.append(idj)
                break

    if (len(s1) == len(imatch) and len(imatch) == len(jmatch)):
        return True
    return False


# print(matchWords("Mary", "Army"))
# print(matchWords("Maryy", "Armyy"))
# print(matchWords("Maryy", "Army"))
# print(matchWords("Marym", "Armyy"))

# 3 TV range from array
def tvRange(arr):
    removeArr = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == 1:
            arr[i] = arr[i] - arr[i] * 2
        elif arr[i] - arr[i - 1] * -1 == 1:
            removeArr.append(i - 1)
            arr[i] = arr[i] - arr[i] * 2
    for j in range(len(removeArr) - 1, -1, -1):
        arr.pop(removeArr[j])
    strArr = ""
    for k in range(len(arr)):
        if k < len(arr) - 1:
            if arr[k] > 0:
                strArr += str(arr[k])
            else:
                strArr += '- ' + str(arr[k] * -1)

            if arr[k + 1] > 0:
                strArr += ', '
            else:
                strArr += ' '
        if k == len(arr) - 1:
            strArr += str(arr[k])

    return strArr


# print(tvRange([1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]))
# print(tvRange([1, 4, 6, 9, 10, 14, 16, 17]))

# 4 reverse pyramid
def pyramidReverse(height):
    for i in range(height):
        for j in range(height * 2):
            if j > i and j < height * 2 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print('\n')


# pyramidReverse(5)

# 5 number triangle
def numTriangle():
    height = int(input("Input : "))
    if height < 1 or height > 4:
        print('input not in range ( 1-4 ) available')
        return

    output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    count = 0
    for i in range(height):
        for j in range(height):
            for l in range(height - i):
                print(' ', end='')
            for k in range(i + 1):
                print(f"{output[count]} ", end='')
                count += 1
            print('\n')
            break


# numTriangle()


# 6 number descending
def numDesc():
    num = input('Input : ')
    number = num.split(',')
    intNum = []
    for idx, i in enumerate(number):
        intNum.append(int(i))

    temp = 0
    for i in range(len(intNum)):
        for j in range(i, len(intNum)):
            if j == i:
                continue
            if intNum[j] > intNum[i]:
                temp = intNum[i]
                intNum[i] = intNum[j]
                intNum[j] = temp
    return intNum


# print(numDesc())

# 7 second to time
import math


def secToTime(second):
    minute = 0
    hour = 0

    if second >= 3600:
        hour = second / 3600
        hour = math.floor(hour)
        second -= hour * 3600
    if second >= 60:
        minute = second / 60
        minute = math.floor(minute)
        second -= minute * 60

    if hour == 0:
        hour = "00"
    elif 0 < hour < 10:
        hour = "0" + str(hour)
    if minute == 0:
        minute = "00"
    elif 0 < minute < 10:
        minute = "0" + str(minute)
    if second == 0:
        second = "00"
    elif 0 < second < 10:
        second = "0" + str(second)
    print(f"{hour}:{minute}:{second}")


# secToTime(59)
# secToTime(90)

# 8 cal change from buying
def calChange(price):
    money = 1000
    change = money - price
    print(f"จำนวนเงินทอน : {change} บาท")

    value = [500, 100, 50, 20, 10, 5, 1]
    num = [0, 0, 0, 0, 0, 0, 0]
    unit = ["ใบ", "ใบ", "ใบ", "ใบ", "เหรียญ", "เหรียญ", "เหรียญ"]

    for idx, i in enumerate(value):
        if change > i:
            num[idx] = change / i
            num[idx] = math.floor(num[idx])
            change -= num[idx] * i

    for idx, i in enumerate(num):
        if i == 0: continue
        print(f"{value[idx]} : {i} {unit[idx]}")


# calChange(32)

# 9 reverse sentence
def reverseSent(sentence):
    sentence = sentence + " "
    reverse = ""
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            for j in range(i - 1, -1, -1):
                if j == 0 or sentence[j - 1] == ' ':
                    for k in range(0, i - j):
                        reverse += sentence[i - k - 1]
                    reverse += " "
                    break

    return reverse


# print(reverseSent("Welcome To clicknext"))

# 10 pyramid
def pyramid(height):
    for i in range(height):
        for j in range(height * 2):
            if j < height + i + 1 and j > height - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print('\n')


# pyramid(5)

# 11 number ascending
def numAsc():
    num = input('Input : ')
    number = num.split(',')
    intNum = []
    for idx, i in enumerate(number):
        intNum.append(int(i))

    temp = 0
    for i in range(len(intNum)):
        for j in range(i, len(intNum)):
            if j == i:
                continue
            if intNum[j] < intNum[i]:
                temp = intNum[i]
                intNum[i] = intNum[j]
                intNum[j] = temp
    return intNum

# print(numAsc())
