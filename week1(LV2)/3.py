
def inp(city, road):
    data = [[None]*city for i in range(city)]
    for i in range (0,road):
        source = input()
        source = source.split(',')
        data[int(source[0])-1][int(source[1])-1] = int(source[2])
        data[int(source[1])-1][int(source[0])-1] = int(source[2])
    # print (data)
    return data

def check(data, city, gone):
    min = 9999
    for i in range(0,len(data[city])):
        # print(i)
        # print('index:',data[city].index(i))
        if i in gone:
            continue
        elif data[city][i] == None:
            continue
        else:
            if data[city][i] <= min:
                min = data[city][i]
                index = i
    # print(data[city].index(min)+1,' : ',min)
    gone.append(index)
    return min

def main():
    temp = input()
    temp = temp.split(',')
    city = int(temp[0])
    road = int(temp[1])
    gone = [0]
    answer = 0
    data = inp(city, road)
    answer = answer + check(data, 0, gone)
    while len(gone) < city:
        flag = 0
        for i in range(0,city):
            if i in gone:
                pass
            else:
                flag = 1
        if flag == 0:
            break
        answer = answer + check(data, gone[-1], gone)
    # print (gone)
    print (answer)

main()
