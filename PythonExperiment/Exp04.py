# a="alex"
# b=a.capitalize()
# #print(a,end=","),print(b)
#
# def func(**p):
#     return "".join((sorted(p)))
# # print(func(x=1,y=2,z=3))
#
# # print("{0:<10}{1:=>10}{1:10}{1:=^10}".format("age","name"))
# print("{:<10}{:<2}c".format("a","b"))
# #print(divmod(x,y))
#
# # lis = [1,2,3,4,5]
# # # print([x for x in lis if x<3])
#
# # print(round(0.1+0.2,3)==0.3)
# # print(24<=28<25)
# # a = "123"
# # b ="123"
# # print(a is b)
import turtle
# def Sum(lis):
#     return sum(lis)
# def fact(m):
#     m = int(m)
#     if m == 1:
#         return m
#     else:
#         return fact(m-1)*m
# def main():
#     m = eval(input("Please Input a integar num: "))
#
#     num = [i for i in range(1,m+1)]
#     jiecheng = []
#     for j in num:
#         jiecheng.append(fact(j))
#     print("fact sum value: %d"%Sum(jiecheng))

def main():
    num = input("请输入一系列整数: ").split(',')
    prim = [i**2 for i in list_prime(*[int(i) for i in num])]  # *[]传入可变参数 不带*为空
    print(prim)
    result = lambda prim:sum(prim)
    print(result(prim))
def list_prime(*n):
    prime = []
    for i in n:
        a=0
        if i==1:
            continue
        if i == 2:
            prime.append(i)
            continue
        for j in range(2,i):
            #print(j,type(j))
                if i%j==0:
                    break
        else:prime.append(i)
    return prime

def numlist():
    return [int(i+1) for i in range(0,26)]
def charlist():
    return [chr(a) for a in range(ord('a'),ord('z')+1)]
def main():
    num = numlist()
    char = charlist()
    dic = {}
    for i in range(0,len(num)):
        dic[num[i]]=char[i]
    print(dic)
    for j in dic.keys():
        if j%2==0:
            print(dic[j],end='  ')

def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    turtle.setup(600,600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level=5
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    turtle.done()

if __name__ == '__main__':
    main()