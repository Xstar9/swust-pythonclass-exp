import jieba
from matplotlib import pyplot as plt # 绘图，可视化
from wordcloud import WordCloud  # 词云
from PIL import Image # 图像处理库
import numpy as np      #矩阵运算

# 词云所需的文本
file = open("source/天龙八部豆瓣短评.txt", "r", encoding="utf-8")

text = "" # 连接文本的字符串
for item in file.readlines():
    text = text + item.strip()
file.close()
print(text.replace("\n",""))

cut = jieba.cut(text) # jieba库分词工具
string =' '.join(cut)

for st in "也是的了在有啊有":
    string = string.replace(st,"")


print(len(string))
print(string)

img = Image.open(r'.\source\loveheart.jpg')
img_array = np.array(img)  # 将图片转化为矩阵数组

wc = WordCloud(
    background_color="white",
    mask=img_array,
    font_path="AdobeKaitiStd-Regular.otf" # C:\Windows\Fonts
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc) # 绘制规则 按词云的规则绘制、
plt.axis("off")   # 不显示坐标轴

# plt.show() #显示生成的词云图片
plt.savefig(r'.\source\wordtest.jpg',dpi=500) # dpi 设置分辨率清晰度