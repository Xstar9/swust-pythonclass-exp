import random

pass_dic={0:"弱",1:"中",2:"强"}

def Read_Data(name):
    dic = {}
    data = []
    with open(name, "r", encoding="utf-8") as file:
        text = file.readline()
        #print(text)
        for i in text:
            if i.isalpha() or i.isdigit():
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
            # print(dic)
        for i in dic.keys():
                if dic[i] == 1:
                    data.append(i)
        # print(data)
        file.close()
    string = "".join(data)
    # print(string)
    return string

# Read_Data("sample.txt")

def Rand_Pass(str):
    ran = random.sample(str,6)
    pwd = "".join(ran)
    # print(pwdlist)
    return pwd

Rand_Pass(Read_Data("sample.txt"))
def Strength_Pass(str):
    string = str
    if string.isdigit():
        key = 0
    if string[0].isalpha():
        key = 1
    if string[0].isdigit() :
        key = 2
    return key


def main():
    data = Read_Data("sample.txt")
    print("密码   强度描述")
    pwdlist = [ Rand_Pass(data) for i in range(0,5)]
    for pwd in pwdlist:
        print("%s   %s"%(pwd,pass_dic[Strength_Pass(pwd)]))

main()