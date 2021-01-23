import random

def test1():
    info = "您的健康状况："
    flag = ['偏瘦','正常','偏胖','肥胖']
    quality = float(input("请输入体重(kg): "))
    height = float(input("请输入身高(m): "))
    BMI = float(quality/pow(height,2))
    print("您的BMI值：%f"%BMI)
    if BMI < 18.5 :
        print(info+''.join(flag[0]))
    elif BMI >= 18.5 and BMI < 25:
        print(info+''.join(flag[1]))
    elif BMI >=25 and BMI <30:
        print(info+''.join(flag[2]))
    else:
        print(info+''.join(flag[3]))

def test2():
    score = int(input("请输入学生成绩："))
    grade = ['A','B','C','D']
    if score>=85 and score <=100:
        print("grade=%s"%grade[0])
    elif score >= 70 and score <85:
        print("grade=%s"%grade[1])
    elif score >=60 and score <70:
        print("grade=%s"%grade[2])
    elif score >0 and score <60:
        print("grade=%s"%grade[3])
    else:
        print("成绩无效！请重新输入(1-100)")
        test2()

def test3():
    N = 0
    num = random.randint(0,10)
    while True:
        guess = int(input("我心里的这个数在0到9之间，你猜这个数是:"))
        if num > guess:
            N += 1
            print("遗憾，太小了")
        elif num < guess:
            N += 1
            print("遗憾，太大了")
        else:
            N +=1
            print("预测%d次，你猜中了！"%N)
            break

def test4():
    text = input("请输入一串字符:")
    cla = ["alpha:","num:","space:","other:"]
    alpha = 0
    num = 0
    space = 0
    other = 0
    for item in text:
        if item.isalpha():
           alpha +=1
        elif item.isdigit():
            num +=1
        elif item.isspace():
            space+=1
        else:
            other+=1
    print("%s%d"%(cla[0],alpha))
    print("%s%d" % (cla[1], num))
    print("%s%d" % (cla[2], space))
    print("%s%d" % (cla[3],other ))

def test31():
    N = 0
    num = random.randint(1, 100+1)
    while True:
        try:
            guess = input("我心里的这个数在0到9之间，你猜这个数是:")
            if guess.count('.')==1:
                N+=1
                print("输入错误,必须输入整数！")
                continue
            guess = int(guess)
            if num > guess:
              N += 1
              print("遗憾，太小了")
            elif num < guess:
                N += 1
                print("遗憾，太大了")
            elif num == guess:
                N += 1
                print("预测%d次，你猜中了！" % N)
                break
        except ValueError:
            print('输入格式错误,结束程序')
            break

def test5():
    num1 = int(input("输入第一个整数："))
    num2 = int(input("输入第二个整数："))
    a = num1
    b = num2
    while b!=0:
        r = a % b
        a = b
        b = r
    print("最大公约数为：%d"%a)
    print("最小公倍数为: %d"%(num1*num2/a))

def test6():
    str1 = "1"
    for i in range(1,10):
        print(str1.center(25," "))
        str1 = str(i+1) + str1 + str(i+1)

test6()







