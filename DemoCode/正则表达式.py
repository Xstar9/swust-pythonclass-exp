import re
import sys
import urllib.request
import xlwt
import bs4
import sqlite3
import urllib.parse

str1 = "South West University of Science and Technology"

'''
# search
pat = re.compile("West")
m = pat.search("WestAABBCCDDAADD")  # search（）----只找到第一次出现的匹配模式，返回位置区间
n = pat.search('AABBCC') # 找不到返回None
print(m)
print(n)
mn = re.search("West", str) # （匹配模式，字符串）
print(mn)

# findall
nm = re.findall("[A-Z]",str)     # findall（"正则表达式"，字符串）-----找到str中所有符合正则表达式的匹配，返回列表
print(nm)
nn = re.findall("[a-z]+",str)    # [a-z]+    匹配多个
print(nn)

# sub  【substitute 替换函数】
str1 = r"a\nBCDE"    # r"~~~"   防转义  即   /n不会被识别成 换行转义
str2 = "a\nBCDE"
mm = re.sub("a","A",str1)    # sub("原字符","替换字符","字符串")  将字符串中的原字符换为替换字符
print(mm)
'''

# 正则表达式：(.*) 就是单个字bai符匹配任意次，即贪du婪匹配; (.*?) 是满足zhi条件的情况只匹配一次，即dao最小匹配.
# re.S 忽略换行等转义符模式
# 图片链接findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)
# 若匹配规则里有1个括号------返回的是括号所匹配到的结果，
# 若匹配规则里有多个括号------返回多个括号分别匹配到的结果，
# findImg = re.compile(r'<img(.*)src="(.*?)"',re.S)  (.*).....(.*?) 会在返回列表时报错 ,can only concatenate str (not "tuple") to str
# 若匹配规则里没有括号------就返回整条语句所匹配到的结果
from bs4 import BeautifulSoup

findImg = re.compile(r'<img.*src="(.*?)"',re.S)                 # 图片
findTitle = re.compile(r'<span class="title">(.*)</span>')      # 标题
findInq =  re.compile(r'<span class="inq">(.*)</span>')         # 概述
findBD = re.compile(r'<p class="">(.*?)</p>',re.S)              # 信息
findScore = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findLink = re.compile(r'<a href="(.*?)">')                      # 链接

def main():
    url = "https://movie.douban.com/top250?start="
    datalist = getData(url)
    # 存入Excel  .xls
    '''
    savepath = "Spider豆瓣电影Top.xls"
    saveData2excel(datalist, savepath)
    '''
    # 存入数据库sqlite3  .db
    saveconnect = sqlite3.connect("Doubanmovies.db")
    #init_DataBase(saveconnect)
    saveData2DataBase(datalist,saveconnect)

def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (WindowsNT10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""   # 定义字符串
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e, code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def getData(baseurl):
    datalist = []
    for i in range(0, 2):
        url = baseurl + str(i * 25)
        # print("-"*100)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        j = 1
        for item in soup.find_all('div', class_="item"):  # div标签里的class_属性值为item
            data = []
            item = str(item)

            Title = re.findall(findTitle, item)[0]
            data.append(Title)

            link = re.findall(findLink, item)[0]  # findall返回的是列表，从遍历item中查找所有findLink [0]---第一个位置
            data.append(link)

            Inq = re.findall(findInq, item)
            if len(Inq)!=0:
                Inq = Inq[0].replace("。","")
                data.append(Inq)
            else:
                data.append("")

            Score=re.findall(findScore,item)[0]
            data.append(Score)

            img = re.findall(findImg, item)[0]
            data.append(img)

            BD = re.findall(findBD, item)[0]
            BD = re.sub('<br(\s+)?\/?>(\s+)?'," ",BD)   # \s  space 空格 \s+ 若干空格    \/?   \表式转义,将'/'转义成一个字符 ?0次或一次
            BD = re.sub('/'," ",BD)
            data.append(BD.strip())   # strip() 消除头尾的空格或()里的指定内容
            j += 1
            datalist.append(data)

    # for i in datalist:
    #     for ii in range(0,5):
    #         print(i[ii])
    return datalist

def saveData2excel(datalist,savepath):
    print("Loading to Save......")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # xlwt.Workbool(解码标准)  创建excel对象
    sheet = book.add_sheet("douban-Top250-movie",cell_overwrite_ok=True)  # 创建一个单元sheet1
    Lie_name = ("影片名","影片链接","影片概述","电影评分","图片链接","相关信息")
    for i in range(0,6):
        sheet.write(0,i,Lie_name[i])
    for j in range(0,50):
        print("爬取到第%d条"%(j+1))
        data = datalist[j]
        for k in range(0,6):
            sheet.write(j+1,k,data[k])

    book.save(savepath)
    print("获取完毕~")

def init_DataBase(saveconnect):
    c = saveconnect.cursor()
    Sql = '''
        create table DouBanMovie
        (id int primary key not null,
        title text not null,
        link text not null,
        inq text not null,
        score text not null,
        img text not null,
        bd text not null
        );
        '''
    c.execute(Sql)  # 执行操作请求
    saveconnect.commit()  # 对象提交数据库的操作
    saveconnect.close()
    print("创建数据库表成功~")

def saveData2DataBase(datalist,saveconnect):
    print("已成功连接到数据库~")
    c = saveconnect.cursor()

    # # 方法1：
    # for data in datalist:
    #     for i in range(len(data)):
    #         data[i] = '"'+data[i]+'"'      #字符化
    #     sql = '''
    #         insert into doubanmovies(id,title,link,inq,img,bd)
    #         values(%d,%s)'''%",".join(data)     # .join  将数据拼接
    #     '''
    #     print(sql)

    for j in range(0,50):
        print("-----------")
        data = datalist[j]

        # 方法2：还可以在数据库直接执行操作：
        # DataBase->目标数据库.db->schemas->main->目标名->右键->SQL Scripts-> Source Editor-> 删除内容->写以下执行语句
        # 方法3
        c.execute(  'insert into DouBanMovie(id,title,link,inq,score,img,bd)values("%d","%s","%s","%s","%s","%s","%s")'
                    %(j, data[0], data[1], data[2], data[3], data[4],data[5])  )
        saveconnect.commit()  # 提交数据库的操作
        print("爬取到第%d条"%(j+1))

    saveconnect.close() # 关闭数据库

if __name__ == '__main__':
    main()









