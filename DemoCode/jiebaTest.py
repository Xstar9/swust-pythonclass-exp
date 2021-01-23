import  jieba # 文本处理分词库
import  re

f = open('for_forever.txt','r',encoding='utf-8')
songword = f.readlines()
# print(songword)
s= ""
for item in songword:
    s = s+item.strip().replace('\n','')
# print(s)

lcut = jieba.lcut(s) # 返回列表类型
print(cut)

cut = jieba.cut(s) # 返回迭代类型
string = ' '.join(cut)
print(string)

# jieba.add_word() 向词库添加新词





