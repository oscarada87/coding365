def inp(city, road):
    data = [[None]*city for i in range(city)]
    for i in range (0,road):
        source = input()
        source = source.split(',')
        data[int(source[0])-1][int(source[1])-1] = int(source[2])
        data[int(source[1])-1][int(source[0])-1] = int(source[2])
    # print (data)
    return data

def getMin(data, gone, number):
    temp = data[number].copy()
    gonecopy = gone.copy()
    gonecopy = sorted(gone, reverse = True)
    # print('goncopy: ', gonecopy)
    for i in gonecopy:
        del temp[i]
    temp.sort()
    # print(temp)
    min = temp[0]
    minIndexList= [i for i, n in enumerate(data[number]) if n == min]
    for i in minIndexList:
        if i in gone:
            pass
        else:
            minIndex = i
    gone.append(minIndex)
    return min

def main():
    temp = input()
    temp = temp.split(',')
    city = int(temp[0])
    road = int(temp[1])
    gone = [0]
    answer = 0
    data = inp(city, road)
    for i in range (4):
        answer = answer + getMin(data, gone, gone[-1])
    print(answer)
    # print(gone)
main()
