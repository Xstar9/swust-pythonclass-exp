from PIL import Image  # python Image Library

img = Image.open("demoIMG.jpg")  # 加载图片文件
'''
    Image.format 图像格式  JEPG JPG PNG
    Image.mode  L灰度图像   RGB   CMYK印刷四色
    Image.size   像素大小
    序列类图像GIF，FLI。。。
    Image.open加载图片自动获取第一帧
    Image.seek() 跳转至指定帧
    Image.tell() 返回当前帧序列号
    Image.save  保存
'''










