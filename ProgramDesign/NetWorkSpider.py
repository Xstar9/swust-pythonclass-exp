import re
import requests
from bs4 import BeautifulSoup

comment = re.compile(r'<span class="short">(.*)</span>')

def main():
    url = "https://book.douban.com/subject/1255625/comments/?start="  # 豆瓣天龙八部短评
    datalist = getData(url)
    export_to_file(datalist)

def askURL(url):
    # 浏览器请求头信息
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        ,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }
    html = ""   # 定义字符串
    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    try:
        html = response.text
        # print(response.text)
    except Exception as e:

        if hasattr(e, "reason"):
            print(e.reason)
    return html

def getData(baseurl):
    datalist = []
    for i in range(0, 10+1):# math.ceil(19245/20)
        url = baseurl + str(i * 20)
        print("-"*100)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        j = 1
        for item in soup.find_all('span', class_="short"):  # div标签里的class_属性值为item
            item = str(item).replace("\n","")
            text = re.findall(comment,item)
            print(j,text)
            j+=1
            datalist.append(text)
    return datalist

def export_to_file(datalist):
    with open('source/天龙八部豆瓣短评.txt', 'a', encoding='utf-8') as file:
        for i in range(0,len(datalist)):
            st = ''.join(datalist[i])
            file.write(st)
            file.write('\n')
            if i%20==0:
                print("导入第{}页".format(int(i/20)+1))

if __name__ == '__main__':
        main()
