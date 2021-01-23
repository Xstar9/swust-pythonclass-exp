def test1():
    k = 1
    h = 5
    for i in range(0,7):
        g = "@"
        if i<4:
            j = g*k
            print(j.center(9,"$"))
            k+=2
        else:
            j = g * h
            print(j.center(9, "$"))
            h-=2



def test2():
    change = []
    while True:
        num = input("请输入4位的整数(1000-9999): ")
        if len(num)!=4 or num[0]=="0":
            print("输入不合法！")
            continue
        else:
            change = []
            for i in range(0,len(num)):
                x = ord(num[i])
                new = (x+5)%10
                change.append(new)
            change[0],change[3]=change[3],change[0]
            change[1], change[2] = change[2], change[1]
            for i in change:
                print(i,end="")
            break


def test3():
    str1 = "fail@ure is probably the fortific&ation in your pole, it is li(ke a peek yo#ur wa+llet as the thief$ when y$ou are thin^king how to spend several hard-won lep#ta wh*en you are wondering whether new money it has laid background because of you then at the heart of the most lax alert and most low awareness and left it, god send failed!"
    str2=str1.replace("@","").replace("^", "").replace("&","").replace("$","").replace(",","").replace("#","").replace("*","").replace("!","").replace("(","").replace("+","")
    lis = str2.split(" ")
    # print(lis)
    dict1 = {}
    for i in lis:
        if i not in dict1.keys():
            dict1[i] = lis.count(i)
    result = sorted(dict1.items(),key=lambda e:e[0])
    # print(result)
    for item in range(-10,0,1):
        result[item]=list(result[item])
        #print(result[item])
        print("{}   {}".format(result[item][0],result[item][1]))

test1()
