#創立一個class
class  University() :
    def __init__(self,name,attributes):
        self.name = name
        self.attributes = attributes


#＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿各種function____________________________________________
def find_the_ans1(k,temp,the_quantity_of_school):
    ans = []
    print(k)
    for i in range(the_quantity_of_school):
        for p in k :
            # print(p)
            if p not in temp[i].attributes :
                ans.append(temp[i].name)
    for i in range(len(temp)) :
        if temp[i].name not in ans :
            print(temp[i].name)

def main():
    # BC(Big Campus)：代表有大校園。
    # NC(Next to City)：代表鄰近有大城市。
    # CT(Convenient Transportation)：代表交通方便。
    # NS(Next to Sea)：代表靠海。
    # NM(Next to Mountain)：代表依山。
    # HL(Has Lake)：代表校園有湖。
    # NL(Near Landscape)：代表附近有風景區。
    temp = []
    the_quantity_of_school = int(input())

    #學校名稱 and 屬性
    for i in range(the_quantity_of_school) :
        a= []
        school = input().strip()
        school = school.split(" ")
        for k in range(1,len(school)):
            a.append(school[k])
        temp.append(University(school[0],a))

    #學生想要的屬性
    wish= int(input())

    for i in range(wish) :
        need = input().strip()
        need = need.split(" + ")
        print(need)
        for k in range(len(need)) :
            if " " in need[k] :
                need[k] = need[k].split(" ")
        print(need)
        for k in need :
            find_the_ans1(k,temp,the_quantity_of_school)


main()
