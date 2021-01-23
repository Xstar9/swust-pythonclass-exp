import itertools
from turtle import *
import time

def test1():
    N = int(input("请输入正整数N: "))
    sum = 0
    numls = [i for i in range(0,N+1)]
    for i in numls:
        sum += i
    print("从1到N的整数和为: %d" % sum)


def test2():
    flag = 1
    result = set()
    vegetable = ["番茄","鸡蛋","土豆","牛肉","鸡肉"]
    # for i in range(len(vegetable)+1):
    #     for item in itertools.combinations(vegetable,i):
    #         result.add(item)
    #         flag+=1
    # print(flag)
    # print(result)
    for i in range(0,len(vegetable)):
        for j in range(0,len(vegetable)):
            if i != j:
                print("第%d道菜名: "%flag+vegetable[i]+vegetable[j])
                flag += 1


def test3():
    color('red','yellow') # pen is red and bk is yellow
    begin_fill()
    while True:
        forward(200)
        right(170)
        if (abs(pos())) < 1:
            break
    end_fill()
    hideturtle()
    done()


def test4():
    str1 = "**"
    j = 0
    for i in range(10):
        j += 1
        y=str1*j
        print(y.center(20))
test4()


def test5():

    power = 1.0
    year = 365
    hard = (power+0.001)**year
    free = (power-0.001)**year
    print("第1小题".center(20,"-"))
    print("每天努力能力值: %f"%hard)
    print("每天放任能力值: %f"%free)
    print("第2小题".center(20,"-"))
    weekday = int(input("请输入今年第一天是星期几(1-7) : "))
    day = year % 7
    week = year//7
    afteryears = ( (power+0.001)**260 * (power-0.001)**104 )
    if weekday+1>=1 and weekday+1 <=5:
        afteryears *= (power+0.001)
    else:
        afteryears *= (power - 0.001)
    print("一年后能力值: %f"%afteryears)


def test6():
    pwd = input("请输入密码：")
    # result = ""
    for alpha in pwd:
        if alpha >= 'A' and alpha <= 'W':
            print(chr(ord(alpha) + 3),end = "")
        elif alpha >= 'X' and alpha <= 'Z':
            print(chr(ord(alpha) -23), end="")
        else:
            print(alpha,end = "")


def test7():
    scale = 50
    print("START".center(scale//2,'-'))
    t = time.clock()
    for i in range(scale+1):
        t -= time.clock()
        a = '*'*i
        b = '.'*(scale-i)
        c = (i/scale)*100
        print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),end="")
        # {} == > 占位
        # := = > 分隔（冒号前部分代表填充的值的标志，后部分代表格式）
        # ^= = > 居中
        # 3.0
        # f == > 数值类型保留位数，3
        # 位整数，0
        # 位小数（修改一下：不是保留3位整数，是字符显示至少3位长度，如果长度不够，补足至3位）
        time.sleep(0.05)
    print("\n"+"OVER".center(scale // 2, '-'))


