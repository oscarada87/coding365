def bin2dec(binList):
    count = 0
    dec = 0
    for i in reversed(binList):
        if int(i) == 1:
            dec = dec + 2 ** count
        else:
            pass
        count = count + 1
    return dec

def dec2bin(number):
    temp = bin(number)
    temp = temp[2:]
    while len(temp) != 11:
        temp = '0'+temp
    return temp

def algo(data, count = 0):
    if data == 0 or data == 1:
        return count
    elif data % 2 == 0:
        count = count + 1
        data = data / 2
        return algo(data, count)
    elif data % 2 == 1:
        count = count + 1
        data = (data + 1) / 2
        return algo(data, count)

def repeatAlgo(number):
    answer = 0
    for i in range (number + 1):
        answer = answer + algo(i)
    return answer

def main():
    str = input()
    data = bin2dec(str)
    # print(data)
    answerbin = repeatAlgo(data)
    print(dec2bin(answerbin))
    while 1:
        interval = input()
        if interval == '-1':
            break
        else:
            pass
        str = input()
        data = bin2dec(str)
        answerbin = repeatAlgo(data)
        print(dec2bin(answerbin))
main()
