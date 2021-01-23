import  json
def test1():
    toDict = []
    toJson = []
    f = open('test.csv','r',encoding='gbk')
    content = f.readline()
    column=content.strip().split(',')
    for i in f.readlines():
        toDict.append(i.strip().split(','))
    for j in range(0,len(toDict)):
        toJson.append(dict(zip(column,toDict[j])))
    print(toJson)
    f.close()

    with open('out.json', 'wb') as ff:
        data = json.dumps(toJson,indent=2,ensure_ascii=False)
        ff.write(data.encode('utf-8'))


#
test1()


def test2():
    # CreateDic()  #先创建词典
    choose = [0,1,2]
    while True:
        try:
            choice = int(input("请输入:(1.添加功能  2.查询功能  0.退出)"))
            if choice not  in choose:
                continue
            if choice == 1:
                addDict()
            elif choice == 2:
                searchDict()
            elif choice == 0:
                print("退出成功")
                break
        except:
            print("输入有误！")

def createDic():
    f = open("英汉词典.txt", "w", encoding="gbk")
    f.write(("{:<12}{:<5}".format("英文单词","中文单词")))
    f.close()

def addDict():
    key = input("请输入英文单词：")
    dic={}
    with open('英汉词典.txt','r',encoding="gbk") as f:
        for line in f:
            line = line.replace("\n"," ").split(" ")
            dic[line[0]] = line[1]

        if key not in dic.keys():
                f.close()
                ff = open('英汉词典.txt', "a")
                value = input("请输入中文单词：")
                # data = key + " " + value + "\n"
                ff.write("{:<12}{:<5}\n".format(key,value))
                ff.close()
                print('添加成功!')
        else:
                f.close()
                print("英文单词已经存在,不能添加")

def searchDict():
    key = input("请输入英文单词：")
    dic = {}
    with open('英汉词典.txt', 'r', encoding="gbk") as f:
        for line in f:
            line = line.replace("\n", "").split()
            dic[line[0]] = line[1]

    if key in dic.keys():
            print("%s的中文释义是：%s"%(key,dic[key]))
    else:
            print("英文单词不在词典中")
    f.close()



# test2()



