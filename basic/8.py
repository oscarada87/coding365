def case183(data):
    total = 0
    total = total + data[0] * 0.08
    total = total + data[1] * 0.139
    total = total + data[2] * 0.135
    total = total + data[3] * 1.128
    total = total + data[4] * 1.483
    if total > 183:
        return int(total)
    else:
        return 183

def case383(data):
    total = 0
    total = total + data[0] * 0.07
    total = total + data[1] * 0.13
    total = total + data[2] * 0.121
    total = total + data[3] * 1.128
    total = total + data[4] * 1.483
    if total > 383:
        return int(total)
    else:
        return 383

def case983(data):
    total = 0
    total = total + data[0] * 0.06
    total = total + data[1] * 0.108
    total = total + data[2] * 0.101
    total = total + data[3] * 1.128
    total = total + data[4] * 1.483
    if total > 983:
        return int(total)
    else:
        return 983

def main():
    data = []
    for i in range(5):
        data.append(int(input()))
    # print(data)
    A = case183(data)
    # print(A)
    B = case383(data)
    # print(B)
    C = case983(data)
    # print(C)
    if A <= B and A <= C:
        print('183')
        print(A)
    elif B <= A and B <= C:
        print('383')
        print(B)
    if C <= B and C <= A:
        print('983')
        print(C)
main()
