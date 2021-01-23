import requests, re
from bs4 import BeautifulSoup

url = "https://www.gushiwen.org/shiju/"
headers = {                      # 响应头
    "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36( KHTML, likeGecko) "
                  "Chrome / 83.0.4103.61Safari / 537.36"
}
response = requests.get(url, headers=headers, timeout=10)
# print(response.status_code)   # 返回网络请求状态码
text = response.text
soup = BeautifulSoup(text, 'lxml')
flag = 0
# print(text)
path = r'C:\zhengxin'
for link in soup.find_all('a', style=" float:left;"):
    if(flag <= 20):
        # print(link)
        if (flag%2==1):
            responses = requests.get(link.get('href'), headers=header)
            texts = responses.text
            soup = BeautifulSoup(texts, 'lxml')
            # print(i)
            try:
                List2 = soup.find_all('h1')
                List2 = List2[0].string
                title = List2.replace('/', '')  # 文件命名不能包含/,空格替换
                 # print(List2)
                full_path = path + '\\' + title + ".txt"
                fb = open(full_path, 'w+', encoding='utf-8')
            except (FileNotFoundError, IndexError):
                pass
            try:
                List3 = soup.find(class_='contson')
                with open(full_path, 'w+') as fb:
                    fb.write(List3.text)
                    print('文档写入完成!')
                    # print(liList3)
                    fb.close()
            except AttributeError:
                pass
    flag += 1
