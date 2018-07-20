# import numpy as np
# import numpy
# print(list_1.intersection(list_2))   # 交集
# print(list_1.union(list_2))          # 聯集
# print(list_1.difference(list_2))     # 差集 in list_1 but not in list_2
# # print(list_1.issubset(list_2))       # 子集
# 集合運算
# list1=[0,1,2,3]
# list2=[2,3,4,5]
# print list(set(list1) & set(list2))　#交集, 輸出[2, 3]
# print list(set(list1) | set(list2))　#聯集, 輸出[0, 1, 2, 3, 4, 5]
# print list(set(list1) ^ set(list2))　#差集, 輸出[0, 1, 4, 5]
aa = []
a = []*20
b = []*20
def numpy01 (typing01,typing02):
    global a,b
    if typing01 == 1:
        a = []
        print(a)
        print(b)
    elif typing01 == 2:
        b = []
        print(a)
        print(b)
    elif typing01 == 3:
        aa = set(a)
        aa.add(typing02)
        a = list(aa)
        print(a)
        print(b)
        # print(aa)
    elif typing01 == 4:
        bb = set()
        bb.add(typing02)
        b = list()
        print(a)
        print(b)
    elif typing01 == 5:
        a.remove(typing02)
        print(a)
        print(b)
    elif typing01 == 6:
        b.remove(typing02)
        print(a)
        print(b)
    elif typing01 == 7:
        print(a.union(b))
    elif typing01 == 8:
        print(a.inrersection(b))
    elif typing01 == 9:
        if a.issubset(b):
            print("1")
        else:
            print("0")
    return typing01

# def numpy02 (typing01):
#     a = []*20
#     b = []*20
#     if typing01 == 7:
#         print(a.union(b))
#     elif typing01 == 8:
#         print(a.inrersetion(b))
#     elif typing01 == 9:
#         if a.issubset(b):
#             print("1")
#         else:
#             print("0")
#     return typing01



def main():

    while True:
        s = input().split(" ")
        typing01 = int(s[0])
        if (len(s)) >1:
            typing02 = int(s[1])
        else:
            typing02 = 0

        if typing01 == 0:
            break
        numpy01(typing01,typing02)
    # print (a)
    # print (b)

    # typing01 = input().split(" ")
    # while True:
    #     if typing01[0] >= 1 and typing01[0] <= 10:


    #         if typing01 == 7:
    #             numpy01 (typing01)
    #         elif typing01 ==8:
    #             numpy01 (typing01)
    #         elif typing01 ==9:
    #             numpy01 (typing01)
    #         elif typing01 == 0:
    #             break

    #     elif  int(typing02)<=100 and int(typing02) <=1:

    #         numpy01(typing01,typing02)

main()
