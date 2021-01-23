import re
import requests
from bs4 import BeautifulSoup

'''软科-中国最好大学排名'''

template = re.compile(r'<td data-v-2a8fd7e4="">(.*?)</td>',re.U) # 正则匹配排名、省份、总分模板
name = re.compile(r'<a data-v-2a8fd7e4="".*>(.*?)</a>') # 正则匹配 学校名称模板

url = "https://www.shanghairanking.cn/rankings/bcur/2020"
headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        ,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }

response = requests.get(url=url,headers=headers)
# 先转成bytes格式在解码 ，否则该网页utf-8直接解码字符仍是乱码（非正常中文字符）
# print(bytes(response.text,response.encoding).decode('utf-8','ignore'))
text = bytes(response.text,response.encoding).decode('utf-8','ignore')
soup = BeautifulSoup(text, "html.parser") # bs4解析html，采用html-parser解析器

file = open(".\Html\中国最好大学.html","w",encoding="utf-8")
file.write(text)
file.close()

print("{1:^2}{2:{0}^9}{3:{0}^6}{4:{0}^5}".format(chr(12288),"排名","名称","省份","总分"))
for item in soup.find_all("tr"):
    item = str(item).replace("<!-- -->","").replace("\n","").replace("          ","") #数据处理，便于正则匹配
    # print(item)
    data = re.findall(template,item)
    Sname = re.findall(name,item)
    if len(data)==0 or len(Sname)==0:
        continue
    level = data[0]
    province = data[1]
    score = data[3]
    # print(level, province, score)
    # print(Sname[0])
    print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}".format(chr(12288),level,Sname[0],province,score))

    # print(Sname)






