import random

def test1():
    code = []
    code.extend([chr(i) for i in range(65, 91)])
    code.extend([chr(i) for i in range(97, 123)])
    code.extend([chr(i) for i in range(48, 58)])
    # print(code)
    pwd = []
    for i in range(0,10):
        pwd.append(''.join([random.choice(code) for i in range(0,8)]))
    for i,p in enumerate(pwd):
        print(i,p)


def test2():
    num = input("输入一系列数字(0为结尾标志):").split(" ")
    numb = [int(i) for i in num]
    print(sorted(numb[:numb.index(0)],reverse=True))


def test3():
    num = int(input("请输入一个大于2的整数:"))
    sushu = []
    for i in range(2,num):
        a = 0
        for j in range(2,i+1):
            if i%j==0:
                a+=1
                if a>1:
                    break
        else:sushu.append(i)
    print((sushu))

def test4():
    num = [i for i in range(0,9+1)]
    words = ["zero","one","two","three","four","five","six","seven","eight","nine",]
    dic = {}
    for j in num:
        dic[j] = words[j]
    # print(dic)
    tel = input("请输入电话号码：")
    print(' '.join([dic[int(i)] for i in tel]))

import jieba
def test5():
    article = open('threekingdoms.txt', 'r', encoding='utf-8').read()
    words = jieba.lcut(article)
    exincludes = ['将军', '却说', '二人', '不可', '荆州', '如此', '不能',
                  '商议', '如何', '主公', '军士', '左右', '军马', '引兵',
                  '次日', '大喜', '天下', '于是', '东吴', '今日', '不敢',
                  '魏兵', '人马', '不知', '汉中', '陛下', '一人', '众将',
                  '只见', '蜀兵', '大叫', '上马', '此人', '后人', '城中',
                  '背后', '一面', '先主', '太守', '大军', '何不', '然后',
                  '忽报', '先生', '夫人', '不如', '先锋', "何故", '江东',
                  '原来', '令人', '天子', '赶来', '徐州', '正是', '忽然',
                  '下马', '因此', '大败', '未知', '百姓', '成都', '大事',
                  '一军', '之后', '起兵', '喊声', '不见', '接应', '引军',
                  '进兵', '引军', '军中', '大怒', '大惊', '可以', '谋反',
                  '心中', '以为', '军民', '不得', '休走', '帐中', '可得']
    nums = {}
    for word in words:
        if len(word) == 1 or word in exincludes:
            continue
        elif word in ['丞相', '曹孟德', '孟德']:
            nums['曹操'] = nums.get('曹操', 0) + 1
        elif word in ['孔明曰', '诸葛亮', '卧龙', '伏龙', '武乡侯', '忠武侯', '蜀相']:
            nums['孔明'] = nums.get('孔明', 0) + 1
        elif word in ['玄德曰', '玄德', '刘豫州', '汉中王', '汉昭烈帝', '平原相', '汉室宗亲', '中山靖王之后', '刘皇叔']:
            nums['刘备'] = nums.get('刘备', 0) + 1
        elif word in ['关公', '云长', '寿亭侯', '关云长']:
            nums['关羽'] = nums.get('关羽', 0) + 1
        elif word in ['都督', '周郎', '公瑾']:
            nums['周瑜'] = nums.get('周瑜', 0) + 1
        elif word in ['飞将', '吕温侯', '奉先', '吕奉先']:
            nums['吕布'] = nums.get('吕布', 0) + 1
        elif word in ['常胜将军', '子龙', '赵子龙']:
            nums['赵云'] = nums.get('赵云', 0) + 1
        else:
            nums[word] = nums.get(word, 0) + 1
    numslist = list(nums.items())

    numslist.sort(key=lambda x: x[1], reverse=True)
    for i in range(20):
        word, count = numslist[i]
        print("{} {} {}".format(i+1,word, count))

import random
def test6():
    hole = [0 for i in range(0,5)]
    move = [1,-1]
    hole[random.randint(0,5)]=1
    day = 1
    now = hole.index(1)
    num = int(input("第%d天,你猜狐狸在0-4号哪个洞里呢: "%day))
    while True:
        if num<0 or num>4:
            num = int(input("撞到墙啦！第%d天,你猜狐狸在0-4号哪个洞里呢: " % day))
        if now == num:
            print("第%d次就抓到了，恭喜！"%day)
            break
        else:
            print("没抓住呢,再接再厉！")
            day+=1
            hole[now]=0
            if now == 0:
                hole[now+1]=1
            elif now == 4:
                hole[now-1]=1
            else:hole[now+random.choice(move)]=1
            num = int(input("第%d天,你猜狐狸在0-4号哪个洞里呢" % day))
test6()


